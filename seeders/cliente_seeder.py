import logging

from .base_seeder import seeder, set_seeder_done
from src.core.errors import read_dependency_csv
from datetime import datetime, timedelta
import pandas as pd
from pathlib import Path
import random

logger = logging.getLogger(__name__)


@seeder(name="clientes", dependencies=["usuarios"], priority=2)
def generate_client_data():
    file = Path("./data/raw/clientes.csv")
    if file.exists():
        logger.info("El archivo ya existe, se omite generación: %s", file)
        return

    users = read_dependency_csv(
        "./data/raw/usuarios.csv", usecols=["id_usuario"], context="clientes"
    )["id_usuario"]

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

    set_seeder_done("clientes", True)