import logging

from .base_seeder import seeder, set_seeder_done
import pandas as pd
from pathlib import Path
import random

logger = logging.getLogger(__name__)


@seeder(name="roles", priority=1)
def generate_role_data ():
    file = Path("./data/raw/roles.csv")

    if file.exists():
        logger.info("El archivo ya existe, se omite generación: %s", file)
        return

    roles = [
        ("Administrador", "Control total del sistema"),
        ("Empleado", "Gestiona pedidos y clientes"),
        ("Cliente", "Realiza compras en la tienda"),
        ("Proveedor", "Suministra productos")
    ]

    data = []

    for i in range(len(roles)):
        data.append([
            i+1,
            roles[i][0],
            roles[i][1]
        ])

    df = pd.DataFrame(data, columns=["id_rol", "rol", "descripcion"])
    df.to_csv(str(file),index=False)

    set_seeder_done("roles", True)