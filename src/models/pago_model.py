from typing import List
from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base

class Pago(Base):
    __tablename__ = 'pagos'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    id_pedido:Mapped[int] = mapped_column(Integer, ForeignKey("pedidos.id"), nullable=False)
    metodo:Mapped[str] = mapped_column(String(255), nullable=False)
    fecha:Mapped[str] = mapped_column(String(255), nullable=False)
    monto:Mapped[str] = mapped_column(String(255), nullable=False)
    estado:Mapped[str] = mapped_column(String(255), nullable=False)

    created_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    pedido:Mapped["Pedido"] = relationship(
        back_populates="pago",
        uselist=False
    )