import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty

logger = logging.getLogger(__name__)


def clean_clientes(df: pd.DataFrame) -> pd.DataFrame:
    require_columns(df, ["id_cliente", "id_usuario", "nivel", "puntos", "fecha_ingreso"], context="clean_clientes")

    df = df.drop_duplicates(subset="id_cliente")

    df["nivel"] = df["nivel"].fillna("Sin nivel")
    df["puntos"] = df["puntos"].fillna(0).astype(int)
    df["fecha_ingreso"] = pd.to_datetime(df["fecha_ingreso"], errors="coerce")

    df = df.dropna(subset=["id_cliente", "id_usuario", "fecha_ingreso"])

    require_non_empty(df, context="clean_clientes")
    logger.info("clientes limpios: %d filas", len(df))
    return df
