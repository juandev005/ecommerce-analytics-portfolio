from typing import List
from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base

class Inventario (Base):
    __tablename__ = 'inventarios'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    id_producto:Mapped[int] = mapped_column(Integer, ForeignKey("productos.id"), nullable=False)
    id_almacen:Mapped[int] = mapped_column(Integer,ForeignKey("almacenes.id"), nullable=False)
    cantidad:Mapped[str] = mapped_column(String(255), nullable=False)
    fecha_ingreso:Mapped[str] = mapped_column(String(255), nullable=False)

    created_at = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    producto:Mapped["Producto"] = relationship(back_populates="inventario")
    almacen:Mapped["Almacen"] = relationship(back_populates="inventario")