from .base_seeder import seeder, set_seeder_done
from src.core.errors import read_dependency_csv
from datetime import datetime, timedelta
import pandas as pd
from pathlib import Path
import random


@seeder(name="empleados", dependencies=["usuarios"], priority=2)
def generate_employee_data():
    file = Path("./data/raw/empleados.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    users = read_dependency_csv(
        "./data/raw/usuarios.csv", usecols=["id_usuario"], context="empleados"
    )["id_usuario"]
    position= [
        "Administrador",
        "Vendedor",
        "Supervisor",
        "Auxiliar de Bodega",
        "Atención al Cliente"
    ]

    data = []

    cantidad_empleados = int(len(users) * 0.20)

    for i in range(cantidad_empleados):
        data.append([
            i+1,
            random.choice(users),
            random.choice(position),
            random.randint(0, 100000),
            datetime.now() - timedelta(days=random.randint(0, 1825))
        ])

    df = pd.DataFrame(data, columns=["id_empleado", "id_usuario", "cargo", "salario", "fecha_contratacion"])
    df.to_csv(str(file), index=False)

    set_seeder_done("empleados", True)