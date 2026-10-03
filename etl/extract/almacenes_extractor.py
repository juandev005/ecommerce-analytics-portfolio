import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_almacenes() -> pd.DataFrame:
    """Lee los datos crudos de almacenes generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/almacenes.csv",
        usecols=['id_almacen', 'almacen', 'ciudad'],
        context="extract_almacenes",
    )
    logger.info("Extraídos %d registros de almacenes", len(df))
    return df
