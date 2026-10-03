import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty

logger = logging.getLogger(__name__)


def clean_categorias(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de categorias: duplicados, tipos y nulos."""
    require_columns(df, ['id_categoria', 'nombre', 'id_categoria_padre'], context="clean_categorias")

    df = df.drop_duplicates(subset="id_categoria")
    df["id_categoria_padre"] = pd.to_numeric(df["id_categoria_padre"], errors="coerce").astype("Int64")

    df = df.dropna(subset=['id_categoria'])

    require_non_empty(df, context="clean_categorias")
    logger.info("categorias limpios: %d filas", len(df))
    return df
