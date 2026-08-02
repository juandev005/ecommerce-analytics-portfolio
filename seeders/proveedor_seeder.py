from faker import Faker
import pandas as pd
from pathlib import Path
import random

def generate_companies_data(cant_of_companies = 1000):
    file = Path("./data/raw/proveedores.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    fake = Faker()

    data = []


    for i in range(cant_of_companies):
        data.append([
            i+1,
            fake.company(),
            fake.company_email(),
            fake.phone_number(),
            random.choice([
                "Colombia",
                "México",
                "Argentina",
                "Chile",
                "Perú",
                "Estados Unidos",
                "España",
                "Brasil"
            ])
        ])

    df = pd.DataFrame(data, columns=["id_proveedor", "nombre", "correo", "telefono", "pais"])
    df.to_csv(str(file),index=False)

generate_companies_data()