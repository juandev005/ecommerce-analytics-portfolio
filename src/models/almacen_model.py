from typing import List
from sqlalchemy import Integer, String, DateTime, Float, func
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base

class Almacen (Base):
    __tablename__ = 'almacenes'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    almacen:Mapped[str] = mapped_column(String(255), nullable=False)
    ciudad:Mapped[str] = mapped_column(String(255), nullable=False)

    created_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    inventario:Mapped[List["Inventario"]] = relationship(
        back_populates="almacen",
        cascade="all, delete-orphan"
    )