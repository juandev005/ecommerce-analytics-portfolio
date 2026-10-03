import logging

from .base_seeder import seeder, set_seeder_done
from src.core.errors import read_dependency_csv, require_columns
import pandas as pd
from pathlib import Path
import random

logger = logging.getLogger(__name__)


@seeder(name="detalle_pedidos", dependencies=["pedidos", "productos"], priority=4)
def generate_order_detail_data():
    file = Path("./data/raw/detalle_pedidos.csv")

    if file.exists():
        logger.info("El archivo ya existe, se omite generación: %s", file)
        return

    orders = read_dependency_csv("./data/raw/pedidos.csv", context="detalle_pedidos")
    require_columns(orders, ["id_pedido", "total"], context="detalle_pedidos (pedidos.csv)")
    products = read_dependency_csv(
        "./data/raw/productos.csv", usecols=["id_producto", "precio"], context="detalle_pedidos"
    )

    data = []

    id_orders = orders.copy()["id_pedido"].to_list()
    prices = products.set_index("id_producto")["precio"].to_dict()

    for i in range(len(orders)):
        id_order = random.choice(id_orders)
        id_product = random.choice(products["id_producto"])
        cantity = random.randint(1, 30)
        price = prices[id_product]
        subtotal = float(round(price * cantity, 2))

        data.append([
            i+1,
            id_order,
            id_product,
            cantity,
            price,
            subtotal
        ])

        id_orders.remove(id_order)

        orders.loc[orders["id_pedido"] == id_order, "total"] += subtotal

    df = pd.DataFrame(data, columns=["id_detalle_pedido", "id_pedido", "id_producto", "cantidad", "precio", "subtotal"])
    df.to_csv(str(file), index=False)
    
    orders.to_csv(("./data/raw/pedidos.csv"), index=False)

    set_seeder_done("detalle_pedidos", True)