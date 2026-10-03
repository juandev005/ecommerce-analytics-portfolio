import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_categorias() -> pd.DataFrame:
    """Lee los datos crudos de categorias generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/categorias.csv",
        usecols=['id_categoria', 'nombre', 'id_categoria_padre'],
        context="extract_categorias",
    )
    logger.info("Extraídos %d registros de categorias", len(df))
    return df
