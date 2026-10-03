import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_roles_usuarios() -> pd.DataFrame:
    """Lee los datos crudos de roles_usuarios generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/roles_usuarios.csv",
        usecols=['id_usuario_rol', 'id_usuario', 'id_rol', 'fecha_ingreso'],
        context="extract_roles_usuarios",
    )
    logger.info("Extraídos %d registros de roles_usuarios", len(df))
    return df
