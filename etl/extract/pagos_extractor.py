import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_pagos() -> pd.DataFrame:
    """Lee los datos crudos de pagos generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/pagos.csv",
        usecols=['id_pago', 'id_pedido', 'metodo', 'fecha', 'monto', 'estado'],
        context="extract_pagos",
    )
    logger.info("Extraídos %d registros de pagos", len(df))
    return df
