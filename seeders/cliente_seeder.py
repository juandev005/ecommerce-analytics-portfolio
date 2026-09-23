from .base import seeder
from datetime import datetime, timedelta
import pandas as pd
from pathlib import Path
import random


@seeder(name="clientes", dependencies=["usuarios"], priority=2)
def generate_client_data():
    file = Path("./data/raw/clientes.csv")
    if file.exists():
        print("El archivo ya existe")
        return

    users = pd.read_csv("./data/raw/usuarios.csv", usecols=["id_usuario"])["id_usuario"]

    levels = [
        "Bronce",
        "Plata",
        "Oro",
        "Platino"
    ]

    data = []
    cant_of_users = int(len(users) * 0.80)

    for i in range(cant_of_users):
        data.append([
            i+1,
            random.choice(users),
            random.choice(levels),
            random.randint(0, 100000),
            datetime.now() - timedelta(days=random.randint(0, 1825))
        ])

    df = pd.DataFrame(data, columns=["id_cliente", "id_usuario", "nivel", "puntos", "fecha_ingreso"])
    df.to_csv(str(file), index=False)