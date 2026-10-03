from typing import List
from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base


class Empleado (Base):
    __tablename__ = 'empleados'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    id_usuario: Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id"))
    cargo: Mapped[str] = mapped_column(String(255), nullable=False)
    salario: Mapped[int] = mapped_column(Integer, nullable=False)
    fecha_contratacion: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[str] =  mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    usuario:Mapped["Usuario"] = relationship(
        back_populates="empleado",
        uselist=False
    )

    pedidos: Mapped[List["Pedido"]] = relationship(back_populates="empleado")