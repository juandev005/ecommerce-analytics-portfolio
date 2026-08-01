from faker import Faker
from pathlib import Path
import random
import pandas as pd

def generate_address(cant_of_addresses = 765):
    fake = Faker('es_CO')
    users = pd.read_csv("./data/raw/usuarios.csv")
    file = Path("./data/raw/direcciones.csv")
    data = []

    if file.exists():
        print("El archivo ya existe")
        return

    for i in range(cant_of_addresses):
        data.append([
            i+1,
            random.choice(users["id_usuario"]),
            "Colombia",
            fake.city(),
            fake.state(),
            fake.postcode(),
            fake.street_address(),
            random.choice([
                "Casa",
                "Trabajo",
                "Facturación"
            ])
        ])

    df = pd.DataFrame(data, columns=["id_direccion", "id_usuario", "pais ciudad", "departamento", "codigo_postal", "direccion", "tipo_direccion"])

    df.to_csv(str(file),index=False)
