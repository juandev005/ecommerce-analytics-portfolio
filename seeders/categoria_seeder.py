import logging

from .base_seeder import seeder, set_seeder_done
import pandas as pd
from pathlib import Path
import random

logger = logging.getLogger(__name__)


@seeder(name="categorias", priority=1)
def generate_category_data():
    file = Path("./data/raw/categorias.csv")

    if file.exists():
        logger.info("El archivo ya existe, se omite generación: %s", file)
        return

    main_categories = [
        "Electrónica",
        "Computación",
        "Celulares",
        "Hogar",
        "Deportes",
        "Moda",
        "Belleza",
        "Libros"
    ]

    subcategories = {
        "Electrónica": ["Televisores", "Audio", "Cámaras"],
        "Computación": ["Laptops", "Monitores", "Accesorios"],
        "Celulares": ["Smartphones", "Fundas", "Cargadores"],
        "Hogar": ["Cocina", "Muebles", "Decoración"],
        "Deportes": ["Fitness", "Ciclismo", "Camping"],
        "Moda": ["Hombre", "Mujer", "Calzado"],
        "Belleza": ["Maquillaje", "Perfumes", "Cuidado Facial"],
        "Libros": ["Novelas", "Tecnología", "Infantiles"]
    }

    data = []
    last_id = 0

    for category in main_categories:
        last_id += 1

        data.append([
            last_id,
            category,
            0
        ])

        id_parent = last_id

        for subcategory in subcategories[category]:
            last_id += 1
            data.append([
                last_id,
                subcategory,
                int(id_parent)
            ])

    df = pd.DataFrame(data, columns=["id_categoria", "nombre", "id_categoria_padre"])
    df.to_csv(str(file),index=False)

    set_seeder_done("categorias", True)