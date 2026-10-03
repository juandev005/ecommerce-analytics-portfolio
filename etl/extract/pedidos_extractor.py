import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_pedidos() -> pd.DataFrame:
    """Lee los datos crudos de pedidos generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/pedidos.csv",
        usecols=['id_pedido', 'id_cliente', 'id_empleado', 'fecha_pedido', 'estado', 'total'],
        context="extract_pedidos",
    )
    logger.info("Extraídos %d registros de pedidos", len(df))
    return df
