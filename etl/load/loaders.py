import logging
import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

from src.core.errors import db_error_boundary
from src.core.exceptions import DatabaseConfigurationError

logger = logging.getLogger(__name__)

load_dotenv()


def _get_engine():
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise DatabaseConfigurationError(
            "La variable de entorno DATABASE_URL no está definida.",
            details={"env_var": "DATABASE_URL"},
        )
    return create_engine(database_url)


def load_to_postgres(df: pd.DataFrame, table_name: str, *, if_exists: str = "replace") -> None:
    engine = _get_engine()
    with db_error_boundary(context=f"carga de '{table_name}'"):
        df.to_sql(table_name, engine, if_exists=if_exists, index=False)
    logger.info("Cargadas %d filas en la tabla '%s'", len(df), table_name)
