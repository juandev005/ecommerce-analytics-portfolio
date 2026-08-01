import pandas as pd
from pathlib import Path
import random


def generate_roles_data ():

    roles = [
        ("Administrador", "Control total del sistema"),
        ("Empleado", "Gestiona pedidos y clientes"),
        ("Cliente", "Realiza compras en la tienda"),
        ("Proveedor", "Suministra productos")
    ]

    file = Path("./data/raw/roles.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    data = []

    for i in range(len(roles)):
        data.append([
            i+1,
            roles[i][0],
            roles[i][1]
        ])

    df = pd.DataFrame(data, columns=["id_rol", "rol", "descripcion"])
    df.to_csv(str(file),index=False)

generate_roles_data()
