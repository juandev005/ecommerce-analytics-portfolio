import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty, normalize_categorical
from etl.transform.enums import MetodoPago, EstadoPago

logger = logging.getLogger(__name__)


def clean_pagos(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de pagos: duplicados, tipos y nulos."""
    require_columns(df, ['id_pago', 'id_pedido', 'metodo', 'fecha', 'monto', 'estado'], context="clean_pagos")

    df = df.drop_duplicates(subset="id_pago")
    df["monto"] = pd.to_numeric(df["monto"], errors="coerce").fillna(0.0).astype(float)
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
    df = normalize_categorical(df, "metodo", MetodoPago, default=MetodoPago.DESCONOCIDO)
    df = normalize_categorical(df, "estado", EstadoPago, default=EstadoPago.DESCONOCIDO)

    df = df.dropna(subset=['id_pago', 'id_pedido', 'fecha'])

    require_non_empty(df, context="clean_pagos")
    logger.info("pagos limpios: %d filas", len(df))
    return df
