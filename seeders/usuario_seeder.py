import logging

from .base_seeder import seeder, set_seeder_done
from src.core.errors import require_positive
from datetime import datetime, timedelta
from faker import Faker
import pandas as pd
from pathlib import Path
import random

logger = logging.getLogger(__name__)


@seeder(name="usuarios", priority=1)
def generate_user_data (cant_of_users = 25000):
    require_positive(cant_of_users, name="cant_of_users")

    file = Path("./data/raw/usuarios.csv")

    if file.exists():
        logger.info("El archivo ya existe, se omite generación: %s", file)
        return

    fake = Faker('es_CO')
    data = []

    for i in range(cant_of_users):
        data.append([
            i+1,
            fake.first_name(),
            fake.last_name(),
            fake.unique.email(),
            fake.phone_number(),
            fake.date_of_birth(minimum_age=18,maximum_age=70),
            datetime.now() - timedelta(days=random.randint(0, 1825)),
            random.choice(["Activo", "Inactivo","Suspendido", None])
        ]
        )

    df = pd.DataFrame(data, columns=["id_usuario", "nombre", "apellido","correo","telefono","fecha_nacimiento","fecha_registro","estado"])
    df.to_csv(str(file),index=False)

    set_seeder_done("usuarios", True)