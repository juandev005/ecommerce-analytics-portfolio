import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty

logger = logging.getLogger(__name__)


def clean_detalle_pedidos(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de detalle_pedidos: duplicados, tipos y nulos."""
    require_columns(df, ['id_detalle_pedido', 'id_pedido', 'id_producto', 'cantidad', 'precio', 'subtotal'], context="clean_detalle_pedidos")

    df = df.drop_duplicates(subset="id_detalle_pedido")
    df["cantidad"] = pd.to_numeric(df["cantidad"], errors="coerce").fillna(0).astype(int)
    df["precio"] = pd.to_numeric(df["precio"], errors="coerce").fillna(0.0).astype(float)
    df["subtotal"] = pd.to_numeric(df["subtotal"], errors="coerce").fillna(0.0).astype(float)

    df = df.dropna(subset=['id_detalle_pedido', 'id_pedido', 'id_producto'])

    require_non_empty(df, context="clean_detalle_pedidos")
    logger.info("detalle_pedidos limpios: %d filas", len(df))
    return df
