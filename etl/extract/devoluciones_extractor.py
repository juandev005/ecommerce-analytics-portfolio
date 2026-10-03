import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_devoluciones() -> pd.DataFrame:
    """Lee los datos crudos de devoluciones generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/devoluciones.csv",
        usecols=['id_devolucion', 'id_pedido', 'motivo', 'estado', 'fecha_devolucion'],
        context="extract_devoluciones",
    )
    logger.info("Extraídos %d registros de devoluciones", len(df))
    return df
