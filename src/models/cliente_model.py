from datetime import datetime
from typing import List
from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base

class Cliente (Base):
    __tablename__ = 'clientes'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    id_usuario:Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id"))
    nivel:Mapped[str] = mapped_column(String(255), nullable=False)
    puntos:Mapped[int] = mapped_column(Integer, nullable=False)
    fecha_ingreso:Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    usuario: Mapped["Usuario"] = relationship(
        back_populates="cliente",
        uselist=False
    )

    pedidos: Mapped[List["Pedido"]] = relationship(back_populates="cliente")

    resenias:Mapped[List["Resenia"]] = relationship(
        back_populates="cliente",
        cascade="all, delete-orphan"
    )