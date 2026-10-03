import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_productos() -> pd.DataFrame:
    """Lee los datos crudos de productos generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/productos.csv",
        usecols=['id_producto', 'id_categoria', 'id_proveedor', 'nombre', 'descripcion', 'precio', 'stock', 'peso', 'estado'],
        context="extract_productos",
    )
    logger.info("Extraídos %d registros de productos", len(df))
    return df
