from faker import Faker
import pandas as pd
from pathlib import Path
import random


def generate_refund_data():
    file = Path("./data/raw/resenias.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    fake = Faker('es_CO')

    clientes = pd.read_csv("./data/raw/clientes.csv")
    products = pd.read_csv("./data/raw/productos.csv")

    data = []

    comentarios = [
        "Excelente producto.",
        "Muy buena calidad.",
        "Lo recomiendo.",
        "Cumple con lo esperado.",
        "Llegó en perfectas condiciones.",
        "Buena relación calidad-precio.",
        "Podría mejorar el empaque.",
        "Muy satisfecho con la compra.",
        "Volvería a comprar.",
        "Producto de excelente calidad."
    ]

    for i in range(int(len(clientes)*0.20)):
        data.append([
            i+1,
            random.choice(clientes["id_cliente"]),
            random.choice(products["id_producto"]),
            random.randint(1, 5),
            random.choice(comentarios),
            fake.date_between(start_date="-1y", end_date="today")
        ])

    df = pd.DataFrame(data, columns=["id_resenia", "id_cliente", "id_producto", "calificacion", "comentario", "fecha"])
    df.to_csv(str(file), index=False)

