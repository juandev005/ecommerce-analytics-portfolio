import logging

from src.core.exceptions import AppError
from src.core.logging_config import configure_logging

from etl.extract.usuarios_extractor import extract_usuarios
from etl.extract.almacenes_extractor import extract_almacenes
from etl.extract.categorias_extractor import extract_categorias
from etl.extract.proveedores_extractor import extract_proveedores
from etl.extract.roles_extractor import extract_roles
from etl.extract.clientes_extractor import extract_clientes
from etl.extract.direcciones_extractor import extract_direcciones
from etl.extract.empleados_extractor import extract_empleados
from etl.extract.productos_extractor import extract_productos
from etl.extract.inventario_extractor import extract_inventario
from etl.extract.pedidos_extractor import extract_pedidos
from etl.extract.roles_usuarios_extractor import extract_roles_usuarios
from etl.extract.detalle_pedidos_extractor import extract_detalle_pedidos
from etl.extract.resenias_extractor import extract_resenias
from etl.extract.pagos_extractor import extract_pagos
from etl.extract.envios_extractor import extract_envios
from etl.extract.factura_extractor import extract_factura
from etl.extract.devoluciones_extractor import extract_devoluciones

from etl.transform.usuarios_transform import clean_usuarios
from etl.transform.almacenes_transform import clean_almacenes
from etl.transform.categorias_transform import clean_categorias
from etl.transform.proveedores_transform import clean_proveedores
from etl.transform.roles_transform import clean_roles
from etl.transform.clientes_transform import clean_clientes
from etl.transform.direcciones_transform import clean_direcciones
from etl.transform.empleados_transform import clean_empleados
from etl.transform.productos_transform import clean_productos
from etl.transform.inventario_transform import clean_inventario
from etl.transform.pedidos_transform import clean_pedidos
from etl.transform.roles_usuarios_transform import clean_roles_usuarios
from etl.transform.detalle_pedidos_transform import clean_detalle_pedidos
from etl.transform.resenias_transform import clean_resenias
from etl.transform.pagos_transform import clean_pagos
from etl.transform.envios_transform import clean_envios
from etl.transform.factura_transform import clean_factura
from etl.transform.devoluciones_transform import clean_devoluciones

from etl.validate.referential_integrity import validate_referential_integrity
from etl.load.loaders import load_to_postgres
from etl.load.schema_mapping import prepare_for_load

logger = logging.getLogger("etl")

PIPELINE = [
    ("usuarios", extract_usuarios, clean_usuarios),
    ("almacenes", extract_almacenes, clean_almacenes),
    ("categorias", extract_categorias, clean_categorias),
    ("proveedores", extract_proveedores, clean_proveedores),
    ("roles", extract_roles, clean_roles),
    ("clientes", extract_clientes, clean_clientes),
    ("direcciones", extract_direcciones, clean_direcciones),
    ("empleados", extract_empleados, clean_empleados),
    ("productos", extract_productos, clean_productos),
    ("inventario", extract_inventario, clean_inventario),
    ("pedidos", extract_pedidos, clean_pedidos),
    ("roles_usuarios", extract_roles_usuarios, clean_roles_usuarios),
    ("detalle_pedidos", extract_detalle_pedidos, clean_detalle_pedidos),
    ("resenias", extract_resenias, clean_resenias),
    ("pagos", extract_pagos, clean_pagos),
    ("envios", extract_envios, clean_envios),
    ("factura", extract_factura, clean_factura),
    ("devoluciones", extract_devoluciones, clean_devoluciones),
]


def run_pipeline() -> None:
    tables: dict = {}

    for name, extract_fn, clean_fn in PIPELINE:
        tables[name] = clean_fn(extract_fn())
        logger.info("Transformado '%s'", name)

    validate_referential_integrity(tables)

    for name, df in tables.items():
        table_name, df = prepare_for_load(name, df)
        load_to_postgres(df, table_name)

    logger.info("Pipeline ETL completado: %d tablas cargadas", len(tables))


if __name__ == "__main__":
    configure_logging()
    try:
        run_pipeline()
    except AppError as exc:
        logger.error("Pipeline falló: %s", exc)
        raise
