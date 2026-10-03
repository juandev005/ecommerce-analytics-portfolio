import logging

import pandas as pd

from src.core.errors import require_columns, require_non_empty

logger = logging.getLogger(__name__)


def clean_empleados(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia los datos crudos de empleados: duplicados, tipos y nulos."""
    require_columns(df, ['id_empleado', 'id_usuario', 'cargo', 'salario', 'fecha_contratacion'], context="clean_empleados")

    df = df.drop_duplicates(subset="id_empleado")
    df["salario"] = pd.to_numeric(df["salario"], errors="coerce").fillna(0).astype(int)
    df["fecha_contratacion"] = pd.to_datetime(df["fecha_contratacion"], errors="coerce")

    df = df.dropna(subset=['id_empleado', 'id_usuario', 'fecha_contratacion'])

    require_non_empty(df, context="clean_empleados")
    logger.info("empleados limpios: %d filas", len(df))
    return df
