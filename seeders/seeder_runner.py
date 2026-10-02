from .base_seeder import get_seeders, get_seeder, set_seeder_done, get_seeders_done
from src.core.exceptions import SeederError, SeederDependencyError, SeederExecutionError, SeederBatchError


def seeding_seeder(name: str) -> None:
    """Ejecuta un único seeder sin resolver dependencias: si falta alguna, falla."""
    seeder_def = get_seeder(name)  # lanza SeederNotFoundError si no existe

    pending_dependencies = [
        dependency for dependency in seeder_def.dependencies
        if not get_seeders_done().get(dependency)
    ]

    if pending_dependencies:
        raise SeederDependencyError(
            f"'{name}' tiene dependencias pendientes: {pending_dependencies}. "
            "Puede que también falten seeders de mayor prioridad.",
            details={"seeder": name, "pendientes": pending_dependencies},
        )

    try:
        seeder_def.execute()
    except Exception as exc:
        raise SeederExecutionError(
            f"Error al ejecutar el seeder '{name}': {exc}",
            details={"seeder": name},
            cause=exc,
        ) from exc

    set_seeder_done(name, True)
    print(f"Seeder '{name}' ejecutado con éxito")


def seeding__with_dependencies(name: str, _resolving: frozenset[str] = frozenset()) -> None:
    """Ejecuta un seeder resolviendo primero, de forma recursiva, sus dependencias pendientes."""
    seeder_def = get_seeder(name)  # lanza SeederNotFoundError si no existe

    if name in _resolving:
        raise SeederDependencyError(
            f"Dependencia circular detectada al resolver '{name}'",
            details={"seeder": name, "cadena": sorted(_resolving)},
        )

    _resolving = _resolving | {name}

    pending_by_priority: dict[int, list[str]] = {}
    for dependency in seeder_def.dependencies:
        if not get_seeders_done().get(dependency):
            dependency_def = get_seeder(dependency)
            pending_by_priority.setdefault(dependency_def.priority, []).append(dependency_def.name)

    for priority in sorted(pending_by_priority):
        for dependency_name in pending_by_priority[priority]:
            # No se envuelve en SeederExecutionError: si ya es un SeederError
            # (dependencia circular, seeder no encontrado, fallo de ejecución),
            # se deja propagar tal cual para no perder la causa real.
            seeding__with_dependencies(dependency_name, _resolving)

    try:
        seeder_def.execute()
    except Exception as exc:
        raise SeederExecutionError(
            f"Error al ejecutar el seeder '{name}': {exc}",
            details={"seeder": name},
            cause=exc,
        ) from exc

    set_seeder_done(name, True)
    print(f"Seeder '{name}' ejecutado con éxito (dependencias: {seeder_def.dependencies})")


def seeding_all() -> None:
    """Ejecuta todos los seeders registrados.

    Comportamiento ante fallos: un seeder roto NO detiene a los demás (fail-soft).
    Cada fallo se registra y se sigue con el siguiente; al final, si hubo alguno,
    se lanza un único SeederBatchError con el resumen de todos.
    """
    errors: dict[str, SeederError] = {}

    for name in get_seeders():
        if get_seeders_done().get(name):
            continue
        try:
            seeding__with_dependencies(name)
        except SeederError as exc:
            print(f"Seeder '{name}' falló: {exc}")
            errors[name] = exc

    if errors:
        raise SeederBatchError(
            f"{len(errors)} seeder(s) fallaron: {sorted(errors)}",
            details={"failures": {k: str(v) for k, v in errors.items()}},
        )

    print("Todos los seeders se ejecutaron con éxito")


if __name__ == "__main__":
    seeding_all()
