import logging

import pandas as pd

from src.core.exceptions import ReferentialIntegrityError

logger = logging.getLogger(__name__)

# (tabla, columna_fk, tabla_referenciada, columna_referenciada)
# Refleja las relaciones declaradas en src/models/.
FOREIGN_KEYS = [
    ("clientes", "id_usuario", "usuarios", "id_usuario"),
    ("direcciones", "id_usuario", "usuarios", "id_usuario"),
    ("empleados", "id_usuario", "usuarios", "id_usuario"),
    ("roles_usuarios", "id_usuario", "usuarios", "id_usuario"),
    ("roles_usuarios", "id_rol", "roles", "id_rol"),
    ("categorias", "id_categoria_padre", "categorias", "id_categoria"),
    ("productos", "id_categoria", "categorias", "id_categoria"),
    ("productos", "id_proveedor", "proveedores", "id_proveedor"),
    ("inventario", "id_producto", "productos", "id_producto"),
    ("inventario", "id_almacen", "almacenes", "id_almacen"),
    ("pedidos", "id_cliente", "clientes", "id_cliente"),
    ("pedidos", "id_empleado", "empleados", "id_empleado"),
    ("detalle_pedidos", "id_pedido", "pedidos", "id_pedido"),
    ("detalle_pedidos", "id_producto", "productos", "id_producto"),
    ("pagos", "id_pedido", "pedidos", "id_pedido"),
    ("envios", "id_pedido", "pedidos", "id_pedido"),
    ("factura", "id_pedido", "pedidos", "id_pedido"),
    ("devoluciones", "id_pedido", "pedidos", "id_pedido"),
    ("resenias", "id_cliente", "clientes", "id_cliente"),
    ("resenias", "id_producto", "productos", "id_producto"),
]


def check_foreign_key(
    df: pd.DataFrame, fk_column: str, ref_df: pd.DataFrame, ref_column: str, *, context: str
) -> None:
    """Verifica que todo valor no nulo de `fk_column` exista en `ref_column` de la tabla referenciada."""
    fk_values = df[fk_column].dropna()
    valid_values = set(ref_df[ref_column].dropna())
    invalid = sorted(set(fk_values) - valid_values)

    if invalid:
        preview = invalid[:10]
        raise ReferentialIntegrityError(
            f"'{context}': {len(invalid)} valor(es) de '{fk_column}' sin correspondencia "
            f"en '{ref_column}' (ej: {preview})",
            details={
                "context": context,
                "fk_column": fk_column,
                "ref_column": ref_column,
                "invalid_count": len(invalid),
                "sample": preview,
            },
        )

    logger.info("Integridad OK: %s (%d valores verificados)", context, len(fk_values))


def validate_referential_integrity(tables: dict[str, pd.DataFrame]) -> None:
    """Verifica todas las relaciones de FOREIGN_KEYS sobre las tablas ya limpias.

    Fail-soft: no se detiene en la primera relación rota, junta todos los fallos
    y al final lanza un único ReferentialIntegrityError con el resumen.
    """
    errors: dict[str, ReferentialIntegrityError] = {}

    for table, fk_column, ref_table, ref_column in FOREIGN_KEYS:
        if table not in tables or ref_table not in tables:
            logger.warning(
                "Se omite relación %s.%s -> %s.%s: tabla no provista", table, fk_column, ref_table, ref_column
            )
            continue

        key = f"{table}.{fk_column} -> {ref_table}.{ref_column}"
        try:
            check_foreign_key(tables[table], fk_column, tables[ref_table], ref_column, context=key)
        except ReferentialIntegrityError as exc:
            logger.error("Integridad referencial falló: %s", exc)
            errors[key] = exc

    if errors:
        raise ReferentialIntegrityError(
            f"{len(errors)} relación(es) con integridad referencial rota: {sorted(errors)}",
            details={"failures": {k: str(v) for k, v in errors.items()}},
        )

    logger.info("Integridad referencial verificada correctamente (%d relaciones)", len(FOREIGN_KEYS))
