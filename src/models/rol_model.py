from .base_model import Base
from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from typing import List


class Rol(Base):
    __tablename__ = 'roles'


    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(255), nullable=False)
    description:Mapped[str] = mapped_column(String(255), nullable=False)
    
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    roles_usuarios: Mapped[list("UsuarioRol")] = relationship(
        back_populates="rol",
        cascade="all, delete-orphan"
    )