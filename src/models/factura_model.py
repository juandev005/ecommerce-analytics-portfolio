from typing import List
from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base

class Factura(Base):
    __tablename__ = 'facturas'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    id_pedido:Mapped[int] = mapped_column(Integer, ForeignKey("pedidos.id"), nullable=False)
    numero:Mapped[int] = mapped_column(String(255), nullable=False)
    fecha_emision:Mapped[int] = mapped_column(String(255), nullable=False)
    impuestos:Mapped[int] = mapped_column(String(255), nullable=False)
    total:Mapped[int] = mapped_column(String(255), nullable=False)

    created_at:Mapped[int] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at:Mapped[int] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    pedido:Mapped["Pedido"] = relationship(
        back_populates="factura",
        uselist=False
    )