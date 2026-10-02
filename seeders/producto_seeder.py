import logging

from .base_seeder import seeder, set_seeder_done
from src.core.errors import require_positive, read_dependency_csv
from faker import Faker
import pandas as pd
from pathlib import Path
import random

logger = logging.getLogger(__name__)


@seeder(name="productos", dependencies=["categorias", "proveedores"], priority=2)
def generate_product_data(cant_of_products = 250000):
    require_positive(cant_of_products, name="cant_of_products")

    file = Path("./data/raw/productos.csv")

    if file.exists():
        logger.info("El archivo ya existe, se omite generación: %s", file)
        return

    fake = Faker('es_CO')

    category_df = read_dependency_csv(
        "./data/raw/categorias.csv", usecols=["id_categoria"], context="productos"
    )
    companies_df = read_dependency_csv(
        "./data/raw/proveedores.csv", usecols=["id_proveedor"], context="productos"
    )

    adjectives = [
        "Premium", "Pro", "Smart", "Ultra", "Max",
        "Mini", "Eco", "Digital", "Plus", "Elite"
    ]

    objects = [
        "Mouse", "Teclado", "Monitor", "Laptop", "Audífonos",
        "Impresora", "Cámara", "Televisor", "Router", "Tablet",
        "Celular", "Silla", "Escritorio", "Lámpara", "Parlante"
    ]

    data = []

    for i in range(cant_of_products):
        data.append([
            i+1,
            random.choice(category_df["id_categoria"]),
            random.choice(companies_df["id_proveedor"]),
            f"{random.choice(adjectives)} {random.choice(objects)}",
            fake.text(max_nb_chars=120),
            round(random.uniform(20, 5000), 2),
            random.randint(0, 500),
            round(random.uniform(0.1, 25.0), 2),
            random.choice([
                "Disponible",
                "Agotado",
                "Descontinuado",
                None
            ])
        ])

    df = pd.DataFrame(data, columns=["id_producto","id_categoria", "id_proveedor", "nombre", "descripcion", "precio", "stock", "peso", "estado"])
    df.to_csv(str(file), index=False)

    set_seeder_done("productos", True)