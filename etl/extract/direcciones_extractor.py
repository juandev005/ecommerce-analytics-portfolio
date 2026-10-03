import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_direcciones() -> pd.DataFrame:
    """Lee los datos crudos de direcciones generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/direcciones.csv",
        usecols=['id_direccion', 'id_usuario', 'pais ciudad', 'departamento', 'codigo_postal', 'direccion', 'tipo_direccion'],
        context="extract_direcciones",
    )
    logger.info("Extraídos %d registros de direcciones", len(df))
    return df
