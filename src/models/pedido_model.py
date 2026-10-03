from datetime import date
from typing import List
from sqlalchemy import Integer, String, Date, DateTime, func, ForeignKey, Float
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base

class Pedido (Base):
    __tablename__ = 'pedidos'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    id_cliente:Mapped[int] = mapped_column(Integer, ForeignKey("clientes.id"), nullable=False)
    id_empleado:Mapped[int] = mapped_column(Integer, ForeignKey("empleados.id"), nullable=False)
    fecha:Mapped[date] = mapped_column(Date, nullable=False)
    estado:Mapped[str] = mapped_column(String(255), nullable=False)
    total:Mapped[float] = mapped_column(Float, nullable=False)

    created_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    cliente:Mapped["Cliente"] = relationship(back_populates="pedidos")
    empleado:Mapped["Empleado"] = relationship(back_populates="pedidos")

    detalle_pedidos:Mapped[List["DetallePedido"]] = relationship(
        back_populates="pedido",
        cascade="all, delete-orphan"
    )

    pago:Mapped["Pago"] = relationship(
        back_populates="pedido",
        uselist=False
    )

    factura:Mapped["Factura"] = relationship(
        back_populates="pedido",
        uselist=False
    )

    envios:Mapped["Envio"] = relationship(
        back_populates="pedido",
        uselist=False
    )

    devoluciones:Mapped[List["Devolucion"]] = relationship(
        back_populates="pedido"
    )