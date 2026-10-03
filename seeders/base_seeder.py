from dataclasses import dataclass, field
from typing import Callable

from src.core.exceptions import SeederError, SeederNotFoundError

@dataclass
class Seeder:
    name: str
    csv_file: str
    dependencies: list[str]
    priority: int
    execute: Callable
    is_done: bool

_SEEDERS_REGISTRY: dict[str, Seeder] = {}

_SEEDERS_DONE_REGISTRY: dict[str, bool] = {}

def seeder(name: str,priority: int = 0, dependencies: list[str] = None, is_done: bool = False):

    def decorator(func: Callable) -> Callable:
        if name in _SEEDERS_REGISTRY:
            raise SeederError(
                f"El seeder '{name}' ya está registrado (dos @seeder con el mismo name)",
                details={"seeder": name},
            )

        seeder_instance = Seeder(
            name=name,
            csv_file=f"./data/raw/{name}.csv",
            dependencies=dependencies or [],
            priority=priority,
            execute=func,
            is_done=is_done
        )

        _SEEDERS_REGISTRY[name] = seeder_instance
        _SEEDERS_DONE_REGISTRY[name] = is_done


        return func
    return decorator

def get_seeders() -> dict[str, Seeder]:
    return _SEEDERS_REGISTRY

def get_seeder(name: str) -> Seeder:
    try:
        return _SEEDERS_REGISTRY[name]
    except KeyError:
        raise SeederNotFoundError(
            f"No se encontró el seeder '{name}'",
            details={"seeder": name, "registrados": sorted(_SEEDERS_REGISTRY)},
        ) from None

def get_seeders_done() -> dict[str, bool]:
    return _SEEDERS_DONE_REGISTRY

def set_seeder_done(name: str, is_done: bool):
    _SEEDERS_DONE_REGISTRY[name] = is_done


exports = [Seeder, seeder, get_seeders, get_seeder, get_seeders_done, set_seeder_done]