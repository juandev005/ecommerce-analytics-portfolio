import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty

logger = logging.getLogger(__name__)


def clean_almacenes(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de almacenes: duplicados, tipos y nulos."""
    require_columns(df, ['id_almacen', 'almacen', 'ciudad'], context="clean_almacenes")

    df = df.drop_duplicates(subset="id_almacen")

    df = df.dropna(subset=['id_almacen'])

    require_non_empty(df, context="clean_almacenes")
    logger.info("almacenes limpios: %d filas", len(df))
    return df
