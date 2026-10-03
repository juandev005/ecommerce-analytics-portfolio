import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_resenias() -> pd.DataFrame:
    """Lee los datos crudos de resenias generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/resenias.csv",
        usecols=['id_resenia', 'id_cliente', 'id_producto', 'calificacion', 'comentario', 'fecha'],
        context="extract_resenias",
    )
    logger.info("Extraídos %d registros de resenias", len(df))
    return df
