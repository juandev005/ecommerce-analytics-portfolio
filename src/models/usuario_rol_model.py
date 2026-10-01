from typing import List
from sqlalchemy import Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base

class UsuarioRol(Base):
    __tablename__ = 'usuarios_roles'
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), primary_key=True)
    rol_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), primary_key=True)
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now()) 
    updated_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    usuario: Mapped["Usuario"] = relationship(
        back_populates="usuario_roles",
        uselist=False
    )
    rol: Mapped["Rol"] = relationship( 
        back_populates="usuario_roles",
        uselist=False
    )