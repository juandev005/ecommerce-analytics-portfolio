from .base_seeder import seeder, set_seeder_done
from src.core.errors import require_positive
from faker import Faker
import pandas as pd
from pathlib import Path
import random


@seeder(name="proveedores", priority=1)
def generate_company_data(cant_of_companies = 1000):
    require_positive(cant_of_companies, name="cant_of_companies")

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

    set_seeder_done("proveedores", True)