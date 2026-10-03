from datetime import date
from typing import List
from sqlalchemy import Integer, String, Date, DateTime, func, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base


class Devolucion(Base):
    __tablename__ = "devoluciones"

    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_pedido:Mapped[int] = mapped_column(Integer, ForeignKey("pedidos.id"), nullable=False,)
    fecha:Mapped[date] = mapped_column(Date, nullable=False)
    motivo:Mapped[str] = mapped_column( String(255), nullable=False)
    estado:Mapped[str] = mapped_column( String(255), nullable=False)

    created_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    pedido:Mapped["Pedido"] = relationship(
        back_populates="devoluciones",
        uselist=False
    )