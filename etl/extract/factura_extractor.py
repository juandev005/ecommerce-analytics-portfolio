import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_factura() -> pd.DataFrame:
    """Lee los datos crudos de factura generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/factura.csv",
        usecols=['id_factura', 'id_pedido', 'numero_factura', 'fecha_emision', 'impuestos', 'total_factura'],
        context="extract_factura",
    )
    logger.info("Extraídos %d registros de factura", len(df))
    return df
