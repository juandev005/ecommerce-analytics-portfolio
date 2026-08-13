from faker import Faker
import pandas as pd
from pathlib import Path
import random

def generate_address_data(cant_of_addresses = 68565):
    file = Path("./data/raw/direcciones.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    fake = Faker('es_CO')
    users = pd.read_csv("./data/raw/usuarios.csv", usecols=["id_usuario"])

    data = []

    for i in range(cant_of_addresses):
        data.append([
            i+1,
            random.choice(users["id_usuario"]),
            "Colombia",
            fake.city(),
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