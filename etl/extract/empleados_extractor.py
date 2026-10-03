import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_empleados() -> pd.DataFrame:
    """Lee los datos crudos de empleados generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/empleados.csv",
        usecols=['id_empleado', 'id_usuario', 'cargo', 'salario', 'fecha_contratacion'],
        context="extract_empleados",
    )
    logger.info("Extraídos %d registros de empleados", len(df))
    return df
