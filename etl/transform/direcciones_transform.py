import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty

logger = logging.getLogger(__name__)


def clean_direcciones(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de direcciones: duplicados, tipos y nulos."""
    require_columns(df, ['id_direccion', 'id_usuario', 'pais ciudad', 'departamento', 'codigo_postal', 'direccion', 'tipo_direccion'], context="clean_direcciones")

    df = df.drop_duplicates(subset="id_direccion")

    df = df.dropna(subset=['id_direccion', 'id_usuario'])

    require_non_empty(df, context="clean_direcciones")
    logger.info("direcciones limpios: %d filas", len(df))
    return df
