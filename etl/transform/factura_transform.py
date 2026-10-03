import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty

logger = logging.getLogger(__name__)


def clean_factura(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de factura: duplicados, tipos y nulos."""
    require_columns(df, ['id_factura', 'id_pedido', 'numero_factura', 'fecha_emision', 'impuestos', 'total_factura'], context="clean_factura")

    df = df.drop_duplicates(subset="id_factura")
    df["impuestos"] = pd.to_numeric(df["impuestos"], errors="coerce").fillna(0.0).astype(float)
    df["total_factura"] = pd.to_numeric(df["total_factura"], errors="coerce").fillna(0.0).astype(float)
    df["fecha_emision"] = pd.to_datetime(df["fecha_emision"], errors="coerce")

    df = df.dropna(subset=['id_factura', 'id_pedido', 'fecha_emision'])

    require_non_empty(df, context="clean_factura")
    logger.info("factura limpios: %d filas", len(df))
    return df
