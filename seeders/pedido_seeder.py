from .base_seeder import seeder, set_seeder_done
from faker import Faker
import pandas as pd
from pathlib import Path
import random


@seeder(name="pedidos", dependencies=["clientes", "empleados"], priority=3)
def generate_order_data(cant_of_orders = 150000):
    file = Path("./data/raw/pedidos.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    fake = Faker()

    customers = pd.read_csv("./data/raw/clientes.csv", usecols=["id_cliente"])["id_cliente"]
    employees = pd.read_csv("./data/raw/empleados.csv", usecols=["id_empleado"])["id_empleado"]



    data = []

    for i in range(cant_of_orders):
        data.append([
            i+1,
            random.choice(customers),
            random.choice(employees),
            fake.date_between(start_date="-2y", end_date="today"),
            "",
            0.0
        ])

    df = pd.DataFrame(data, columns=["id_pedido", "id_cliente", "id_empleado", "fecha_pedido", "estado", "total"])
    df.to_csv(str(file), index=False)

    set_seeder_done("pedidos", True)
