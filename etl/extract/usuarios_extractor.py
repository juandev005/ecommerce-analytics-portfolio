import logging

import pandas as pd

from src.core.errors import read_dependency_csv

logger = logging.getLogger(__name__)


def extract_usuarios() -> pd.DataFrame:
    """Lee los datos crudos de usuarios generados por el seeder. Sin transformar."""
    df = read_dependency_csv(
        "./data/raw/usuarios.csv",
        usecols=['id_usuario', 'nombre', 'apellido', 'correo', 'telefono', 'fecha_nacimiento', 'fecha_registro', 'estado'],
        context="extract_usuarios",
    )
    logger.info("Extraídos %d registros de usuarios", len(df))
    return df
