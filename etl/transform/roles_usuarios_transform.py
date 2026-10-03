import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty

logger = logging.getLogger(__name__)


def clean_roles_usuarios(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de roles_usuarios: duplicados, tipos y nulos."""
    require_columns(df, ['id_usuario_rol', 'id_usuario', 'id_rol', 'fecha_ingreso'], context="clean_roles_usuarios")

    df = df.drop_duplicates(subset="id_usuario_rol")
    df["fecha_ingreso"] = pd.to_datetime(df["fecha_ingreso"], errors="coerce")

    df = df.dropna(subset=['id_usuario_rol', 'id_usuario', 'id_rol', 'fecha_ingreso'])

    require_non_empty(df, context="clean_roles_usuarios")
    logger.info("roles_usuarios limpios: %d filas", len(df))
    return df
