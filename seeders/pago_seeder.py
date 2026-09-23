from .base import seeder
from faker import Faker
import pandas as pd
from pathlib import Path
import random

@seeder(name="pagos", dependencies=["pedidos", "facturas"], priority=4)
def generate_payment_data():
    file = Path("./data/raw/pagos.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    fake = Faker('es_CO')

    orders_csv = pd.read_csv("./data/raw/pedidos.csv")
    bill_csv = pd.read_csv("./data/raw/factura.csv", usecols=["id_pedido", "total_factura"])

    orders =  orders_csv[["id_pedido"]]

    data = []

    methods = [
        "Tarjeta Crédito",
        "Tarjeta Débito",
        "PSE",
        "Transferencia",
        "Efectivo"
    ]

    payment_status = [
        "Pendiente",
        "Aprobado",
        "Rechazado"
    ]
    
    for i in range(len(orders)):

        pay_status = random.choice(payment_status)
        id_order = orders["id_pedido"][i]

        data.append([
            i+1,
            id_order,
            random.choice(methods),
            fake.date_between(start_date="-2y",end_date="today"),
            round((bill_csv[bill_csv["id_pedido"] == id_order]["total_factura"].values[0]), 2),
            pay_status
        ])

        match pay_status:
            case "Aprobado":
                orders_csv.loc[orders_csv["id_pedido"] == id_order, "estado"] = random.choice(["Pagado","Enviado","Entregado", "Pendiente"])
            case "Rechazado":
                orders_csv.loc[orders_csv["id_pedido"] == id_order, "estado"] = "Cancelado"
            case "Pendiente":
                orders_csv.loc[orders_csv["id_pedido"] == id_order, "estado"] = "Pendiente"

    df = pd.DataFrame(data, columns=["id_pago", "id_pedido", "metodo",  "fecha", "monto", "estado"])
    df.to_csv(str(file), index=False)
    orders_csv.to_csv("./data/raw/pedidos.csv", index=False)