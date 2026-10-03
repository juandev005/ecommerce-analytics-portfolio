import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty, normalize_categorical
from etl.transform.enums import EstadoUsuario

logger = logging.getLogger(__name__)


def clean_usuarios(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de usuarios: duplicados, tipos y nulos."""
    require_columns(df, ['id_usuario', 'nombre', 'apellido', 'correo', 'telefono', 'fecha_nacimiento', 'fecha_registro', 'estado'], context="clean_usuarios")

    df = df.drop_duplicates(subset="id_usuario")
    df["fecha_nacimiento"] = pd.to_datetime(df["fecha_nacimiento"], errors="coerce")
    df["fecha_registro"] = pd.to_datetime(df["fecha_registro"], errors="coerce")
    df = normalize_categorical(df, "estado", EstadoUsuario, default=EstadoUsuario.DESCONOCIDO)

    df = df.dropna(subset=['id_usuario', 'fecha_nacimiento', 'fecha_registro'])

    require_non_empty(df, context="clean_usuarios")
    logger.info("usuarios limpios: %d filas", len(df))
    return df
