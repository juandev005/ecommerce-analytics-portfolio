import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_inventario() -> pd.DataFrame:
    """Lee los datos crudos de inventario generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/inventario.csv",
        usecols=['id_inventario', 'id_producto', 'id_almacen', 'cantidad', 'fecha_ingreso'],
        context="extract_inventario",
    )
    logger.info("Extraídos %d registros de inventario", len(df))
    return df
