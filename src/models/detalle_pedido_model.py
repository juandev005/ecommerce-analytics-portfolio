from typing import List
from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base

class DetallePedido (Base):
    __tablename__ = 'detalle_pedidos'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    id_pedido:Mapped[int] = mapped_column(Integer,ForeignKey("pedidos.id"), nullable=False )
    id_producto:Mapped[int] = mapped_column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad:Mapped[str] = mapped_column(String(255), nullable=False)
    precio_unitario:Mapped[str] = mapped_column(String(255), nullable=False)
    subtotal:Mapped[str] = mapped_column(String(255), nullable=False)

    created_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    pedido:Mapped["Pedido"] = relationship(back_populates="detalle_pedidos")
    producto:Mapped["Producto"] = relationship(back_populates="detalle_pedidos")