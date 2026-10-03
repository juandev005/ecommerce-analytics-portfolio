import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_roles() -> pd.DataFrame:
    """Lee los datos crudos de roles generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/roles.csv",
        usecols=['id_rol', 'rol', 'descripcion'],
        context="extract_roles",
    )
    logger.info("Extraídos %d registros de roles", len(df))
    return df
