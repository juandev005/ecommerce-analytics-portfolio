from faker import Faker
import pandas as pd
from pathlib import Path 
import random



def generate_refund_data():
    file = Path("./data/raw/devoluciones.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    fake = Faker('es_CO')

    orders = pd.read_csv("./data/raw/pedidos.csv", usecols=["id_pedido", "estado"])
    orders_delivered = orders[orders["estado"] == "Cancelado"]

    data = []

    motivos = [
        "Producto defectuoso",
        "Producto equivocado",
        "No cumplió expectativas",
        "Empaque dañado",
        "Llegó incompleto",
        "Cambio de opinión"
    ]

    estados = [
        "Pendiente",
        "Aprobada",
        "Rechazada",
        "Finalizada"
    ]

    ids_pedidos = orders_delivered["id_pedido"].to_list()

    for i in range(len(ids_pedidos)):
        data.append([
            i+1,
            ids_pedidos[i],
            random.choice(motivos),
            random.choice(estados),
            fake.date_between(start_date="-2y", end_date="today")
        ])

    df = pd.DataFrame(data, columns=["id_devolucion", "id_pedido", "motivo", "estado", "fecha_devolucion"])
    df.to_csv(str(file), index=False)