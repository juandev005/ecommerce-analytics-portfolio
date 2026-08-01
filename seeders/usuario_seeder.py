from faker import Faker
import random
import pandas as pd
from pathlib import Path


def generate_random_user_data (cant_of_users = 1000):
    
    file = Path("./data/raw/usuarios.csv")

    if file.exists():
        print("El archivo ya existe")
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
            fake.date_between(start_date="-5y",end_date="today"),
            random.choice(["Activo", "Inactivo","Suspendido", None])
        ]
        )


    df = pd.DataFrame(data, columns=["id_usuario", "nombre", "apellido","correo","telefono","fecha_nacimiento","fecha_registro","estado"])

    df.to_csv(str(archivo),index=False)

generate_random_user_data(10000)

