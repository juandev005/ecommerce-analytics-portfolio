from typing import List
from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base

class Resenia(Base):
    __tablename__ = 'resenias'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    id_producto:Mapped[int] = mapped_column(Integer, ForeignKey("productos.id"), nullable=False)
    id_cliente:Mapped[int] = mapped_column(Integer, ForeignKey("clientes.id"), nullable=False)
    calificacion:Mapped[str] = mapped_column(String(255), nullable=False)
    comentario:Mapped[str] = mapped_column(String(255), nullable=False)
    fecha:Mapped[str] = mapped_column(String(255), nullable=False)

    created_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    producto:Mapped["Producto"] = relationship(
        back_populates="resenias",
        uselist=False
    )
    cliente:Mapped["Cliente"] = relationship(
        back_populates="resenias",
        uselist=False
    )