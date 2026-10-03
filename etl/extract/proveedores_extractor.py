import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_proveedores() -> pd.DataFrame:
    """Lee los datos crudos de proveedores generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/proveedores.csv",
        usecols=['id_proveedor', 'nombre', 'correo', 'telefono', 'pais'],
        context="extract_proveedores",
    )
    logger.info("Extraídos %d registros de proveedores", len(df))
    return df
