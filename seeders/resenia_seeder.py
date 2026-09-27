from .base import seeder
from faker import Faker
import pandas as pd
from pathlib import Path
import random
from  .base import set_seeder_done

@seeder(name="resenias", dependencies=["pedidos", "detalle_pedidos"], priority=3)
def generate_review_data():
    file = Path("./data/raw/resenias.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    fake = Faker('es_CO')

    orders = pd.read_csv("./data/raw/pedidos.csv", usecols=["id_pedido","id_cliente", "estado"])
    orders_details = pd.read_csv("./data/raw/detalle_pedidos.csv", usecols=["id_pedido", "id_producto"])

    orders_delivered = orders[orders["estado"] == "Entregado"].to_dict("list")

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

    for i in range(int(len(orders_delivered["id_pedido"])*0.60)):


        id_client = orders_delivered["id_cliente"][i]
        id_pedido = orders_delivered["id_pedido"][i]
        id_product = orders_details[orders_details["id_pedido"] == id_pedido].to_dict("list")["id_producto"][0]

        data.append([
            i+1,
            id_client,
            id_product,
            random.randint(1, 5),
            random.choice(comentarios),
            fake.date_between(start_date="-1y", end_date="today")
        ])

    df = pd.DataFrame(data, columns=["id_resenia", "id_cliente", "id_producto", "calificacion", "comentario", "fecha"])
    df.to_csv(str(file), index=False)

    set_seeder_done("resenias", True)