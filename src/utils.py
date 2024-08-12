import json
import os
from typing import Any, Dict, List

from config import DATA_DIR


def get_data_from_json(filename: str) -> List[Dict[str, Any]]:
    """Функция чтения и парсинга данных из json файла"""

    full_path = os.path.join(DATA_DIR, filename)
    with open(full_path, "r", encoding="UTF-8") as file:
        data_json = json.load(file)
    return data_json



# if __name__ == "__main__":
#     data_to_obj = data_from_json("products.json")
#     print(data_to_obj)
