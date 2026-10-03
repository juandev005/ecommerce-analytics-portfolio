import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty

logger = logging.getLogger(__name__)


def clean_resenias(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de resenias: duplicados, tipos y nulos."""
    require_columns(df, ['id_resenia', 'id_cliente', 'id_producto', 'calificacion', 'comentario', 'fecha'], context="clean_resenias")

    df = df.drop_duplicates(subset="id_resenia")
    df["calificacion"] = pd.to_numeric(df["calificacion"], errors="coerce").fillna(0).astype(int)
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

    df = df.dropna(subset=['id_resenia', 'id_cliente', 'id_producto', 'fecha'])

    require_non_empty(df, context="clean_resenias")
    logger.info("resenias limpios: %d filas", len(df))
    return df
