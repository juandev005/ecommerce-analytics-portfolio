class AppError(Exception):
    def __init__(self, message: str, *, details: dict | None = None, cause: Exception | None = None):
        self.details = details or {}
        self.cause = cause       # la excepción original (SQLAlchemy, pandas, etc.)
        super().__init__(message)