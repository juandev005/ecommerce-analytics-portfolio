from faker import Faker
import pandas as pd
from pathlib import Path
import random


def generate_payment_data():
    file = Path("./data/raw/pagos.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    fake = Faker('es_CO')

    pedidos = pd.read_csv("./data/raw/pedidos.csv")


    data = []

    metodos = [
        "Tarjeta Crédito",
        "Tarjeta Débito",
        "PSE",
        "Transferencia",
        "Efectivo"
    ]

    estados = [
        "Pendiente",
        "Aprobado",
        "Rechazado"
    ]

    for i in range(len(pedidos)):

        data.append([
            i+1,
            pedidos["id_pedido"][i],
            random.choice(metodos),
            fake.date_between(
                start_date="-2y",
                end_date="today"
            ),
            pedidos["total"][i],
            random.choice(estados)
        ])


    df = pd.DataFrame(data, columns=["id_pago", "id_pedido", "metodo",  "fecha", "monto", "estado"])
    df.to_csv(str(file), index=False)

generate_payment_data()


for i in range(10):
    pedidos = pd.read_csv("./data/raw/pedidos.csv")
    print(pedidos["id_pedido"])