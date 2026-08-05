from faker import Faker
import pandas as pd
from pathlib import Path
import random

def generate_order_data(cant_of_orders = 15000):
    file = Path("./data/raw/pedidos.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    fake = Faker('es_CO')

    customers = pd.read_csv("./data/raw/clientes.csv")["id_cliente"]
    employees = pd.read_csv("./data/raw/empleados.csv")["id_empleado"]

    states = [
        "Pendiente",
        "Pagado",
        "Enviado",
        "Entregado",
        "Cancelado"
    ]

    data = []

    for i in range(cant_of_orders):
        data.append([
            i+1,
            random.choice(customers),
            random.choice(employees),
            fake.date_between(start_date="-2y", end_date="today"),
            random.choice(states),
            0.0
        ])

    df = pd.DataFrame(data, columns=["id_pedido", "id_cliente", "id_empleado", "fecha_pedido", "estado", "total"])
    df.to_csv(str(file), index=False)
