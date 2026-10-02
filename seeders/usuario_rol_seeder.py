from .base_seeder import seeder, set_seeder_done
from src.core.errors import read_dependency_csv
from faker import Faker
import pandas as pd
from pathlib import Path
import random

@seeder(name="roles_usuarios", dependencies=["usuarios", "roles", "empleados", "clientes"], priority=3)
def generate_role_user_data():
    file = Path("./data/raw/roles_usuarios.csv")

    if file.exists():
        print("El archivo ya existe")
        return

    fake = Faker('es_CO')

    roles = read_dependency_csv(
        "./data/raw/roles.csv", usecols=["id_rol", "rol"], context="roles_usuarios"
    )

    employees = read_dependency_csv(
        "./data/raw/empleados.csv", usecols=["id_empleado"], context="roles_usuarios"
    )
    customers = read_dependency_csv(
        "./data/raw/clientes.csv", usecols=["id_cliente"], context="roles_usuarios"
    )

    roles_employees = roles[roles.rol.isin(["Administrador", "Empleado"])].id_rol.values
    roles_customers = roles[roles.rol.isin(["Cliente", "Proveedor"])].id_rol.values
    

    data = []

    count = 0
    prev_rol = 0

    for employee in employees.id_empleado:
        has_other_rol = random.choice([True, False])

        while True:
            count += 1
            
            if has_other_rol:
                i = random.choice(roles_employees)
                prev_rol = i
            else:
                available_roles = set(roles_employees).difference({prev_rol})
                i = random.choice(list(available_roles))


            data.append([
                count,
                employee,
                i,
                fake.date_between(start_date="-5y",end_date="today")
            ])

            if not has_other_rol:
                break

            has_other_rol = False


    for user in customers.id_cliente:
        has_other_rol = random.choice([True, False])

        while True:
            count += 1

            if has_other_rol:
                i = random.choice(roles_customers)
                prev_rol = i
            else:
                available_roles = set(roles_customers).difference({prev_rol})
                i = random.choice(list(available_roles))


            data.append([
                count,
                user,
                i,
                fake.date_between(start_date="-5y",end_date="today")
            ])

            if not has_other_rol:
                break

            has_other_rol = False

    df = pd.DataFrame(data, columns=["id_usuario_rol","id_usuario", "id_rol", "fecha_ingreso"])
    df.to_csv(str(file),index=False)

    set_seeder_done("roles_usuarios", True)