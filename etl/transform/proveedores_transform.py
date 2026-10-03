import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty

logger = logging.getLogger(__name__)


def clean_proveedores(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de proveedores: duplicados, tipos y nulos."""
    require_columns(df, ['id_proveedor', 'nombre', 'correo', 'telefono', 'pais'], context="clean_proveedores")

    df = df.drop_duplicates(subset="id_proveedor")

    df = df.dropna(subset=['id_proveedor'])

    require_non_empty(df, context="clean_proveedores")
    logger.info("proveedores limpios: %d filas", len(df))
    return df
