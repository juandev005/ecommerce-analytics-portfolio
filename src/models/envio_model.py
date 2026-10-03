from datetime import date
from typing import List
from sqlalchemy import Integer, String, Date, DateTime, func, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base

class Envio (Base):
    __tablename__ = 'envios'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    id_pedido:Mapped[int] = mapped_column(Integer, ForeignKey("pedidos.id"), nullable=False)
    id_direccion:Mapped[int] = mapped_column(Integer, ForeignKey("direcciones.id"), nullable=False)
    empresa:Mapped[int] = mapped_column(String(255), nullable=False)
    numero:Mapped[int] = mapped_column(String(255), nullable=False)
    fecha_envio:Mapped[date] = mapped_column(Date, nullable=False)
    fecha_entrega:Mapped[date] = mapped_column(Date, nullable=False)
    estado:Mapped[int] = mapped_column(String(255), nullable=False)

    created_at:Mapped[int] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at:Mapped[int] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    pedido:Mapped["Pedido"] = relationship(
        back_populates="envios",
        uselist=False
    )
    
    direccion:Mapped["Direccion"] = relationship(
        back_populates="envios",
        uselist=False
    )