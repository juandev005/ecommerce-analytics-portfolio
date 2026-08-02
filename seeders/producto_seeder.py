from faker import Faker
import pandas as pd
from pathlib import Path
import random

def generate_product(cant_of_products = 50000):
    file = Path("./data/raw/productos.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    fake = Faker('es_CO')

    category_df = pd.read_csv("./data/raw/categorias.csv")
    companies_df = pd.read_csv("./data/raw/proveedores.csv")

    id_categories = category_df["id_categoria"]
    id_companies = companies_df["id_proveedor"]

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
            i,
            random.choice(id_categories),
            random.choice(id_companies),
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