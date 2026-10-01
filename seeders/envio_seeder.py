from .base_seeder import seeder, set_seeder_done
from faker import Faker
import pandas as pd
from pathlib import Path
import random


@seeder(name="envios", dependencies=["pedidos", "direcciones"], priority=4)
def generate_shipment_data():
    file = Path("./data/raw/envios.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    fake = Faker('es_CO')

    transportadoras = [
        "Servientrega",
        "Coordinadora",
        "Inter Rapidísimo",
        "Deprisa",
        "Envía"
    ]

    orders_csv = pd.read_csv("./data/raw/pedidos.csv")
    address = pd.read_csv("./data/raw/direcciones.csv", usecols=["id_direccion", "id_usuario"])

    orders = pd.concat([
        orders_csv[orders_csv["estado"] == "Enviado"],
        orders_csv[orders_csv["estado"] == "Entregado"]
    ], ignore_index=True).to_dict("list")

    data = []

    for i in range(len(orders["id_pedido"])):

        id_usuario = orders["id_cliente"][i]
        id_pedido = orders["id_pedido"][i]

        direcciones_usuario = address.loc[address["id_usuario"] == id_usuario, "id_direccion"].tolist()

        if direcciones_usuario:
            direccion = random.choice(direcciones_usuario)
            estado = random.choice(["Preparando","En tránsito","Entregado"])
        else:
            direccion = random.choice([0, None, " ", "   "])
            orders_csv.loc[orders_csv["id_pedido"] == id_pedido, "estado"] = "Pendiente"
            estado = "Preparando"

        fecha_envio = fake.date_between(start_date="-2y", end_date="today")
        fecha_entrega = fake.date_between(start_date="-715d", end_date="today")


        data.append([
            i+1,
            id_pedido,
            direccion,
            random.choice(transportadoras),
            fake.unique.bothify("GUIA########"),
            fecha_envio,
            fecha_entrega,
            estado
        ])

    df = pd.DataFrame(data, columns=["id_envio", "id_pedido", "direccion", "transportadora", "guia", "fecha_envio", "fecha_entrega", "estado"])
    df.to_csv(str(file), index=False)
    orders_csv.to_csv("./data/raw/pedidos.csv", index=False)

    set_seeder_done("envios",True)