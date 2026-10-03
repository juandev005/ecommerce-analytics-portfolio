import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_detalle_pedidos() -> pd.DataFrame:
    """Lee los datos crudos de detalle_pedidos generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/detalle_pedidos.csv",
        usecols=['id_detalle_pedido', 'id_pedido', 'id_producto', 'cantidad', 'precio', 'subtotal'],
        context="extract_detalle_pedidos",
    )
    logger.info("Extraídos %d registros de detalle_pedidos", len(df))
    return df
