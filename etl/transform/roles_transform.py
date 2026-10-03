import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty

logger = logging.getLogger(__name__)


def clean_roles(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de roles: duplicados, tipos y nulos."""
    require_columns(df, ['id_rol', 'rol', 'descripcion'], context="clean_roles")

    df = df.drop_duplicates(subset="id_rol")

    df = df.dropna(subset=['id_rol'])

    require_non_empty(df, context="clean_roles")
    logger.info("roles limpios: %d filas", len(df))
    return df
