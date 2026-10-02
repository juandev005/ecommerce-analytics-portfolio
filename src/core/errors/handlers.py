from contextlib import contextmanager
from pathlib import Path

import pandas as pd
from sqlalchemy.exc import IntegrityError, OperationalError, SQLAlchemyError

from src.core.exceptions import (
    DatabaseConnectionError,
    DatabaseError,
    DatabaseIntegrityError,
    FieldValidationError,
    SchemaValidationError,
    SeederFileError,
)

def require_columns(df: pd.DataFrame, expected: list[str], *, context: str) -> None:
    missing = sorted(set(expected) - set(df.columns))
    if missing:
        raise SchemaValidationError(
            f"Faltan columnas {missing} en los datos de '{context}'",
            details={"missing_columns": missing, "context": context},
        )


def require_non_empty(df: pd.DataFrame, *, context: str) -> None:
    if df.empty:
        raise SchemaValidationError(
            f"Los datos de '{context}' están vacíos",
            details={"context": context},
        )


def require_positive(value: int, *, name: str) -> None:
    if value <= 0:
        raise FieldValidationError(
            f"'{name}' debe ser un valor positivo, se recibió {value}",
            details={"field": name, "value": value},
        )


def read_dependency_csv(path: str, *, usecols: list[str] | None = None, context: str) -> pd.DataFrame:
    file = Path(path)

    if not file.exists():
        raise SeederFileError(
            f"No se encontró '{file}', requerido por '{context}'. "
            "Ejecuta primero el seeder que lo genera.",
            details={"file": str(file), "context": context},
        )

    try:
        df = pd.read_csv(file, usecols=usecols)
    except ValueError as exc:
        raise SchemaValidationError(
            f"'{file}' no tiene las columnas esperadas {usecols} ({context})",
            details={"file": str(file), "expected_columns": usecols, "context": context},
            cause=exc,
        ) from exc
    except (pd.errors.ParserError, OSError) as exc:
        raise SeederFileError(
            f"No se pudo leer '{file}' ({context})",
            details={"file": str(file), "context": context},
            cause=exc,
        ) from exc

    require_non_empty(df, context=context)
    return df


@contextmanager
def db_error_boundary(session=None, *, context: str = "operación de base de datos"):
    try:
        yield
    except IntegrityError as exc:
        if session is not None:
            session.rollback()
        raise DatabaseIntegrityError(
            f"Violación de integridad en {context}", cause=exc
        ) from exc
    except OperationalError as exc:
        if session is not None:
            session.rollback()
        raise DatabaseConnectionError(
            f"No se pudo conectar/operar con la base de datos durante {context}", cause=exc
        ) from exc
    except SQLAlchemyError as exc:
        if session is not None:
            session.rollback()
        raise DatabaseError(
            f"Error inesperado de base de datos durante {context}", cause=exc
        ) from exc
