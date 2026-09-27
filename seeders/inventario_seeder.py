from .base import seeder
from faker import Faker
import pandas as pd
from pathlib import Path
import random
from  .base import set_seeder_done

@seeder(name="inventario", dependencies=["productos", "almacenes"], priority=3)
def generate_inventory_data(cant_of_products = 175000):
    file = Path("./data/raw/inventario.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    fake = Faker()

    products = pd.read_csv("./data/raw/productos.csv", usecols=["id_producto"]).id_producto
    warehouses = pd.read_csv("./data/raw/almacenes.csv", usecols=["id_almacen"]).id_almacen

    data = []

    for i in range(cant_of_products):

        id_product = random.choice(products)
        id_stored_product = random.choice(warehouses)

        data.append([
                i+1,
                id_product,
                id_stored_product,
                random.randint(1, 1000),
                fake.date_between(start_date="-5y",end_date="today")
        ])

    df = pd.DataFrame(data, columns=["id_inventario", "id_producto", "id_almacen", "cantidad", "fecha_ingreso"])
    df.to_csv(str(Path("./data/raw/inventario.csv")), index=False)

    set_seeder_done("inventario", True)