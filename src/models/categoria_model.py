from typing import List, Optional
from sqlalchemy import Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from .base_model import Base

class Categoria (Base):
    __tablename__ = 'categorias'

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre:Mapped[str] = mapped_column(String(255), nullable=False)
    id_categoria_padre:Mapped[Optional[int]] = mapped_column(ForeignKey("categorias.id"))
    
    created_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at:Mapped[str] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())


    categoria_padre: Mapped[Optional["Categoria"]] = relationship( 
        remote_side=[id], 
        back_populates="subcategorias"
    )

    subcategorias: Mapped[List["Categoria"]] = relationship( 
        back_populates="categoria_padre"
    )

    productos:Mapped[List["Producto"]] = relationship(
        back_populates="categoria",
    )