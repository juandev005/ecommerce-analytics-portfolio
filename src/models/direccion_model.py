from .base_model import Base
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from typing import List, Optional


class Direccion(Base):
    __tablename__ = 'direcciones'
    id: Mapped[int] = mapped_column(primary_key=True)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("usuarios.id"),nullable=False)
    pais: Mapped[str] = mapped_column(String(255), nullable=False)
    ciudad: Mapped[str] = mapped_column(String(255), nullable=False)
    departamento: Mapped[str] = mapped_column(String(255), nullable=False)
    codigo_postal: Mapped[str] = mapped_column(String(255), nullable=False)
    calle: Mapped[str] = mapped_column(String(255), nullable=False)
    tipo: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[str] = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[str] = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    usuario: Mapped["Usuario"] = relationship( back_populates="direcciones")
    envios: Mapped[List["Envio"]] = relationship(back_populates="direccion")