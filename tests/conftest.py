import pytest

from src.product import Product, Category, Smartphone, LawnGrass


@pytest.fixture
def product_1():
    return Product(name="Холодильник", description="Холодильник LG", price=30000, quantity=5)


@pytest.fixture
def product_2():
    return {"name": "Холодильник", "description": "Холодильник LG", "price": 30000, "quantity": 5}


@pytest.fixture
def product_3():
    return Product(name="Насос", description='Насос автомобильный "Силач 3000"', price=4000, quantity=25)


@pytest.fixture
def product_4():
    return Product(name="Насос", description='Насос автомобильный "Силач 3000"', price=4000, quantity=0)


@pytest.fixture
def category_1():
    return Category(
        name="Бытовая техника",
        description="Техника для дома и быта",
        products=[
            Product("Холодильник", "Холодильник LG", 30000, quantity=5),
            Product("Плита", "Плита Искорка", 10000, quantity=10),
            Product("СВЧ", "СВЧ LG", 5000, quantity=15),
        ],
    )


@pytest.fixture
def category_2():
    return Category(
        name="Мобильная техника",
        description="Телефоны, планшеты, риддеры",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000, quantity=5),
            Product("Iphone 15", "512GB, Gray space", 210000, quantity=8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000, quantity=14),
        ],
    )


@pytest.fixture
def category_3():
    return Category(
        name="Товары для автомобиля",
        description="Акссесуары для вашего автомобиля",
        products=[Product("Насос", 'Насос автомобильный "Силач 3000"', 3000, quantity=25)],
    )


@pytest.fixture
def json_data():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]

@pytest.fixture
def fake_product():
    return "fake_product"


@pytest.fixture
def smartphone_1():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone_2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 12, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawngrass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass_2():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 10, "Россия", "7 дней", "Зеленый")