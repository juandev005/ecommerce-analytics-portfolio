import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty

logger = logging.getLogger(__name__)


def clean_productos(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de productos: duplicados, tipos y nulos."""
    require_columns(df, ['id_producto', 'id_categoria', 'id_proveedor', 'nombre', 'descripcion', 'precio', 'stock', 'peso', 'estado'], context="clean_productos")

    df = df.drop_duplicates(subset="id_producto")
    df["precio"] = pd.to_numeric(df["precio"], errors="coerce").fillna(0.0).astype(float)
    df["stock"] = pd.to_numeric(df["stock"], errors="coerce").fillna(0).astype(int)
    df["peso"] = pd.to_numeric(df["peso"], errors="coerce").fillna(0.0).astype(float)

    df = df.dropna(subset=['id_producto', 'id_categoria', 'id_proveedor'])

    require_non_empty(df, context="clean_productos")
    logger.info("productos limpios: %d filas", len(df))
    return df
