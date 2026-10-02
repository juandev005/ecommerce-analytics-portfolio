import logging

from .base_seeder import seeder, set_seeder_done
from src.core.errors import read_dependency_csv
from faker import Faker
import pandas as pd
from pathlib import Path
import random

logger = logging.getLogger(__name__)


@seeder(name="facturas", dependencies=["pedidos"], priority=4)
def generate_bill_data():
    file = Path("./data/raw/factura.csv")

    if file.exists():
        logger.info("El archivo ya existe, se omite generación: %s", file)
        return

    fake = Faker()

    orders = read_dependency_csv(
        "./data/raw/pedidos.csv", usecols=["id_pedido", "total"], context="facturas"
    ).to_dict("list")

    data = []

    for i in range(len(orders["id_pedido"])):

        subtotal = orders["total"][i]
        impuestos = round(subtotal * 0.19, 2)
        total_factura = round(subtotal + impuestos, 2)

        data.append([
            i+1,
            orders["id_pedido"][i],
            fake.unique.bothify("FAC-######"),
            fake.date_between(
                start_date="-2y",
                end_date="today"
            ),
            impuestos,
            total_factura
        ])

    df = pd.DataFrame(data, columns=["id_factura", "id_pedido", "numero_factura", "fecha_emision", "impuestos", "total_factura"])
    df.to_csv(str(file), index=False)

    set_seeder_done("facturas", True)
