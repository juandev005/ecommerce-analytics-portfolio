import logging

from .base_seeder import seeder, set_seeder_done
from src.core.errors import require_positive, read_dependency_csv
from faker import Faker
import pandas as pd
from pathlib import Path
import random

logger = logging.getLogger(__name__)


@seeder(name="direcciones", dependencies=["usuarios"], priority=2)
def generate_address_data(cant_of_addresses = 68565):
    require_positive(cant_of_addresses, name="cant_of_addresses")

    file = Path("./data/raw/direcciones.csv")

    if file.exists():
        logger.info("El archivo ya existe, se omite generación: %s", file)
        return

    fake = Faker('es_CO')
    users = read_dependency_csv(
        "./data/raw/usuarios.csv", usecols=["id_usuario"], context="direcciones"
    )

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

    set_seeder_done("direcciones", True)