import logging
import pandas as pd
from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_clientes() -> pd.DataFrame:

    df = read_dependency_csv(
        "./data/raw/clientes.csv",
        usecols=["id_cliente", "id_usuario", "nivel", "puntos", "fecha_ingreso"],
        context="extract_clientes",
    )
    logger.info("Extraídos %d registros de clientes", len(df))
    return df
