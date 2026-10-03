import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty, normalize_categorical
from etl.transform.enums import EstadoEnvio

logger = logging.getLogger(__name__)


def clean_envios(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de envios: duplicados, tipos y nulos."""
    require_columns(df, ['id_envio', 'id_pedido', 'direccion', 'transportadora', 'guia', 'fecha_envio', 'fecha_entrega', 'estado'], context="clean_envios")

    df = df.drop_duplicates(subset="id_envio")
    df["fecha_envio"] = pd.to_datetime(df["fecha_envio"], errors="coerce")
    df["fecha_entrega"] = pd.to_datetime(df["fecha_entrega"], errors="coerce")
    df = normalize_categorical(df, "estado", EstadoEnvio, default=EstadoEnvio.DESCONOCIDO)

    df = df.dropna(subset=['id_envio', 'id_pedido', 'fecha_envio'])

    require_non_empty(df, context="clean_envios")
    logger.info("envios limpios: %d filas", len(df))
    return df
