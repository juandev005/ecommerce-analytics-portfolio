import logging

import pandas as pd

logger = logging.getLogger(__name__)

ID_COLUMNS = {
    "usuarios": "id_usuario",
    "almacenes": "id_almacen",
    "categorias": "id_categoria",
    "proveedores": "id_proveedor",
    "roles": "id_rol",
    "clientes": "id_cliente",
    "direcciones": "id_direccion",
    "empleados": "id_empleado",
    "productos": "id_producto",
    "inventario": "id_inventario",
    "pedidos": "id_pedido",
    "detalle_pedidos": "id_detalle_pedido",
    "resenias": "id_resenia",
    "pagos": "id_pago",
    "envios": "id_envio",
    "factura": "id_factura",
    "devoluciones": "id_devolucion",
}

TABLE_NAME_OVERRIDES = {
    "inventario": "inventarios",
    "factura": "facturas",
    "roles_usuarios": "usuarios_roles",
}

COLUMN_RENAMES = {
    "roles": {"rol": "name", "descripcion": "description"},
    "direcciones": {
        "pais ciudad": "pais",
        "departamento": "ciudad",
        "direccion": "calle",
        "tipo_direccion": "tipo",
    },
    "pedidos": {"fecha_pedido": "fecha"},
    "detalle_pedidos": {"precio": "precio_unitario"},
    "roles_usuarios": {"id_usuario": "usuario_id", "id_rol": "rol_id"},
    "envios": {"direccion": "id_direccion", "transportadora": "empresa", "guia": "numero"},
    "factura": {"numero_factura": "numero", "total_factura": "total"},
    "devoluciones": {"fecha_devolucion": "fecha"},
}

DROP_COLUMNS = {
    "roles_usuarios": ["id_usuario_rol"],
}

DEFAULT_VALUES = {
    "direcciones": {"departamento": "Sin dato"},
}


def prepare_for_load(name: str, df: pd.DataFrame) -> tuple[str, pd.DataFrame]:
    """Adapta un DataFrame ya limpio al esquema real de la base de datos (src/models)."""
    df = df.copy()

    if name in ID_COLUMNS:
        df = df.rename(columns={ID_COLUMNS[name]: "id"})

    if name in COLUMN_RENAMES:
        df = df.rename(columns=COLUMN_RENAMES[name])

    if name == "envios":
        df["id_direccion"] = pd.to_numeric(df["id_direccion"], errors="coerce").astype("Int64")
        sin_direccion = df["id_direccion"].isna().sum()
        if sin_direccion:
            logger.warning("envios: se descartan %d filas sin id_direccion valido", sin_direccion)
        df = df.dropna(subset=["id_direccion"])

    for column in DROP_COLUMNS.get(name, []):
        df = df.drop(columns=[column])

    for column, value in DEFAULT_VALUES.get(name, {}).items():
        df[column] = value

    table_name = TABLE_NAME_OVERRIDES.get(name, name)
    return table_name, df
