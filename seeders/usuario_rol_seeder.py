from faker import Faker
import pandas as pd
from pathlib import Path
import random

def generate_user_rol_data():
    file = Path("./data/raw/roles_usuarios.csv")

    if file.exists(): 
        print("El archivo ya existe")
        return

    fake = Faker('es_CO')

    users = pd.read_csv("./data/raw/usuarios.csv")
    roles = pd.read_csv("./data/raw/roles.csv")
    list_of_roles = roles.id_rol

    data = []

    for i in users.id_usuario:
        j = random.randint(0, len(list_of_roles)-1)
        k = random.randint(0, 1)

        while True:
            data.append([
                i,
                list_of_roles[j],
                fake.date_between(start_date="-5y",end_date="today")
            ])

            if k == 1:
                break

            k+=1

    df = pd.DataFrame(data, columns=["id_usuario", "id_rol", "fecha_ingreso"])
    df.to_csv(str(file),index=False)