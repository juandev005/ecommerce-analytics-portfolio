import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty, normalize_categorical
from etl.transform.enums import MotivoDevolucion, EstadoDevolucion

logger = logging.getLogger(__name__)


def clean_devoluciones(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de devoluciones: duplicados, tipos y nulos."""
    require_columns(df, ['id_devolucion', 'id_pedido', 'motivo', 'estado', 'fecha_devolucion'], context="clean_devoluciones")

    df = df.drop_duplicates(subset="id_devolucion")
    df["fecha_devolucion"] = pd.to_datetime(df["fecha_devolucion"], errors="coerce")
    df = normalize_categorical(df, "motivo", MotivoDevolucion, default=MotivoDevolucion.DESCONOCIDO)
    df = normalize_categorical(df, "estado", EstadoDevolucion, default=EstadoDevolucion.DESCONOCIDO)

    df = df.dropna(subset=['id_devolucion', 'id_pedido', 'fecha_devolucion'])

    require_non_empty(df, context="clean_devoluciones")
    logger.info("devoluciones limpios: %d filas", len(df))
    return df
