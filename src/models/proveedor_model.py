from typing import List, Optional
from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base

class Proveedor(Base):
    __tablename__ = 'proveedores'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre:Mapped[str] = mapped_column(String(255), nullable=False)
    correo:Mapped[str] = mapped_column(String(255), nullable=False)
    telefono:Mapped[str] = mapped_column(String(255), nullable=False)
    pais:Mapped[str] = mapped_column(String(255), nullable=False)

    created_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    productos:Mapped[List["Producto"]] = relationship(back_populates="proveedor")