import json
import os
from typing import Any, Dict, List

from config import DATA_DIR

from src.product import Product, Category


def data_from_json(filename: str) -> List[Dict[str, Any]]:
    full_path = os.path.join(DATA_DIR, filename)
    with open(full_path, "r", encoding="UTF-8") as file:
        data_json = json.load(file)
    return data_json


def objects_from_data(data: List[Dict]) -> List:
    categories = []
    for category in data:
        products_list = []
        for product in category["products"]:
            products_list.append(Product(**product))
        category["products"] = products_list
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    data_to_obj = data_from_json("products.json")
    print(data_to_obj)
    objects = objects_from_data(data_to_obj)
    print(objects)
    print(objects[1].name)
    print(objects[1].description)
    print(objects[1].category_count)
    print(objects[0].product_count)
    print(objects[1].product_count)