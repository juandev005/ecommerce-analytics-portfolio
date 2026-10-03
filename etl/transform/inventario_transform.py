import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty

logger = logging.getLogger(__name__)


def clean_inventario(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de inventario: duplicados, tipos y nulos."""
    require_columns(df, ['id_inventario', 'id_producto', 'id_almacen', 'cantidad', 'fecha_ingreso'], context="clean_inventario")

    df = df.drop_duplicates(subset="id_inventario")
    df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce").fillna(0).astype(int)
    df["fecha_ingreso"] = pd.to_datetime(df["fecha_ingreso"], errors="coerce")

    df = df.dropna(subset=['id_inventario', 'id_producto', 'id_almacen', 'fecha_ingreso'])

    require_non_empty(df, context="clean_inventario")
    logger.info("inventario limpios: %d filas", len(df))
    return df
