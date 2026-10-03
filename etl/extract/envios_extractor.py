import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_envios() -> pd.DataFrame:
    """Lee los datos crudos de envios generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/envios.csv",
        usecols=['id_envio', 'id_pedido', 'direccion', 'transportadora', 'guia', 'fecha_envio', 'fecha_entrega', 'estado'],
        context="extract_envios",
    )
    logger.info("Extraídos %d registros de envios", len(df))
    return df
