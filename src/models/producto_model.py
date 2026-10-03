from typing import List
from sqlalchemy import Integer, String, DateTime, Float, func, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base


class Producto (Base):
    __tablename__ = 'productos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_categoria: Mapped[int] = mapped_column(Integer, ForeignKey("categorias.id"), nullable=False)
    id_proveedor: Mapped[int] = mapped_column(Integer, ForeignKey("proveedores.id"), nullable=False)
    nombre: Mapped[str] = mapped_column(String(255), nullable=False)
    descripcion: Mapped[str] = mapped_column(String(255), nullable=False)
    precio: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    estado: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    categoria: Mapped["Categoria"] = relationship(back_populates="productos")
    proveedor: Mapped["Proveedor"] = relationship(back_populates="productos")

    inventario:Mapped[List["Inventario"]] = relationship(
        back_populates="producto",
        cascade="all, delete-orphan"
    )

    detalle_pedidos:Mapped[List["DetallePedido"]] = relationship(
        back_populates="producto",
        cascade="all, delete-orphan"
    )

    resenias:Mapped[List["Resenia"]] = relationship(
        back_populates="producto",
        cascade="all, delete-orphan"
    )