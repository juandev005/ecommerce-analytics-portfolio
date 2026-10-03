import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty

logger = logging.getLogger(__name__)


def clean_pedidos(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de pedidos: duplicados, tipos y nulos."""
    require_columns(df, ['id_pedido', 'id_cliente', 'id_empleado', 'fecha_pedido', 'estado', 'total'], context="clean_pedidos")

    df = df.drop_duplicates(subset="id_pedido")
    df["total"] = pd.to_numeric(df["total"], errors="coerce").fillna(0.0).astype(float)
    df["fecha_pedido"] = pd.to_datetime(df["fecha_pedido"], errors="coerce")

    df = df.dropna(subset=['id_pedido', 'id_cliente', 'id_empleado', 'fecha_pedido'])

    require_non_empty(df, context="clean_pedidos")
    logger.info("pedidos limpios: %d filas", len(df))
    return df
