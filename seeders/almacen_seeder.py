from .base_seeder import seeder, set_seeder_done
from faker import Faker
import pandas as pd
from pathlib import Path
import random

@seeder(name="almacenes", priority=1)
def generate_warehouse_data(cant_of_warehouses = 50):

    fake = Faker('es_CO')

    file = Path("./data/raw/almacenes.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    warehouses = [
        "Almacén Norte", 
        "Almacén Centro",
        "Almacén Sur", 
        "Almacén Oriente", 
        "Almacén Occidente"
    ]

    data = []

    for i in range(cant_of_warehouses):
        data.append([
            i+1,
            random.choice(warehouses),
            fake.city()
        ])

    df = pd.DataFrame(data, columns=["id_almacen", "almacen", "ciudad"])
    df.to_csv("./data/raw/almacenes.csv", index=False)

    set_seeders_done("almacenes", True)