from typing import List
from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base


class Usuario(Base):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(255), nullable=False)
    apellido: Mapped[str] = mapped_column(String(255), nullable=False)
    correo: Mapped[str] = mapped_column(String(255), nullable=False)
    telefono: Mapped[str] = mapped_column(String(255), nullable=False)
    fecha_nacimiento: Mapped[str] = mapped_column(String(255), nullable=False)
    fecha_registro: Mapped[str] = mapped_column(String(255), nullable=False)
    estado: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    direcciones: Mapped[List["Direccion"]] = relationship(
        back_populates="usuario",
        cascade="all, delete-orphan"
    )

    usuario_roles: Mapped[List["UsuarioRol"]] = relationship(
        back_populates="usuario",
        cascade="all, delete-orphan"
    )

    cliente:Mapped["Cliente"] = relationship(
        back_populates="usuario",
        uselist=False,
        cascade="all, delete-orphan"
    )

    empleado:Mapped["Empleado"] = relationship(
        back_populates = "usuario",
        uselist=False
    )