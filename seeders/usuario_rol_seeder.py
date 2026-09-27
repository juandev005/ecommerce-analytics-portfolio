from .base import seeder
from faker import Faker
import pandas as pd
from pathlib import Path
import random
from  .base import set_seeder_done

@seeder(name="roles_usuarios", dependencies=["usuarios", "roles"], priority=2)
def generate_user_role_data():
    file = Path("./data/raw/roles_usuarios.csv")

    if file.exists(): 
        print("El archivo ya existe")
        return

    fake = Faker('es_CO')

    users = pd.read_csv("./data/raw/usuarios.csv", usecols=["id_usuario"])
    roles = pd.read_csv("./data/raw/roles.csv", usecols=["id_rol"])

    data = []

    count = 0

    for user in users.id_usuario:
        has_other_rol = random.choice([True, False])

        while True:
            count += 1
            i = random.randint(1, len(roles)-1)

            data.append([
                count,
                user,
                roles.iloc[i,0],
                fake.date_between(start_date="-5y",end_date="today")
            ])

            if not has_other_rol:
                break

            has_other_rol = False

    df = pd.DataFrame(data, columns=["id_usuario_rol","id_usuario", "id_rol", "fecha_ingreso"])
    df.to_csv(str(file),index=False)

    set_seeder_done("roles_usuarios", True)