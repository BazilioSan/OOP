from unittest.mock import patch

import pytest

from src.order import Order
from src.product import Category, LawnGrass, Product, Smartphone


def test_product_creation():
    product = Product("iPhone 13", "The latest iPhone model", 999.99, 10)
    assert product.name == "iPhone 13"
    assert product.description == "The latest iPhone model"
    assert product.price == 999.99
    assert product.quantity == 10


def test_new_product_creation():
    product_data = {
        "name": "Samsung Galaxy S21",
        "description": "The latest Samsung flagship",
        "price": 799.99,
        "quantity": 15,
    }
    product = Product.new_product(product_data)
    assert product.name == "Samsung Galaxy S21"
    assert product.description == "The latest Samsung flagship"
    assert product.price == 799.99
    assert product.quantity == 15


def test_product_price_change():
    with patch("builtins.input", return_value="y"):
        product = Product("iPhone 13", "The latest iPhone model", 999.99, 10)
        product.price = 899.99
        assert product.price == 899.99


def test_category_creation():
    product1 = Product("iPhone 13", "The latest iPhone model", 999.99, 10)
    product2 = Product("Samsung Galaxy S21", "The latest Samsung flagship", 799.99, 15)
    category = Category("Smartphones", "Smartphones for communication and more", [product1, product2])
    assert category.name == "Smartphones"
    assert category.description == "Smartphones for communication and more"
    assert category.products_list == [product1, product2]
    assert category.product_count == 2
    assert category.category_count == 1


def test_str_category(category_1):
    assert str(category_1) == "Бытовая техника, количество продуктов: 30 шт."


def test_category_str(category_3):
    assert category_3.products == "Насос, 3000 руб. Остаток: 25 шт.\n"


def test_add_product(product_1, product_3):
    assert product_1 + product_3 == 250000


def test_str_product(product_1):
    assert str(product_1) == "Холодильник, 30000 руб. Остаток: 5 шт."

def test_add_category_not_product(category_3, fake_product):
    with pytest.raises(TypeError):
        category_3.add_product(fake_product)


def test_lawn_grass_init(lawngrass_1):
    assert lawngrass_1.name == "Газонная трава"
    assert lawngrass_1.description == "Элитная трава для газона"
    assert lawngrass_1.price == 500.0
    assert lawngrass_1.quantity == 20
    assert lawngrass_1.country == "Россия"
    assert lawngrass_1.germination_period == "7 дней"
    assert lawngrass_1.color == "Зеленый"


def test_lawn_grass_add(lawngrass_1, lawngrass_2):
    assert lawngrass_1 + lawngrass_2 == 15000.0


def test_lawn_grass_add_not_grass(lawngrass_1, smartphone_1):
    with pytest.raises(TypeError):
        lawngrass_1 + smartphone_1


def test_smartphone_init(smartphone_1):
    assert smartphone_1.name == "Iphone 15"
    assert smartphone_1.description == "512GB, Gray space"
    assert smartphone_1.price == 210000.0
    assert smartphone_1.quantity == 8
    assert smartphone_1.efficiency == 98.2
    assert smartphone_1.model == "15"
    assert smartphone_1.memory == 512
    assert smartphone_1.color == "Gray space"


def test_smartphone_add(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 4200000.0


def test_smartphone_add_not_smartphone(smartphone_1, lawngrass_1):
    with pytest.raises(TypeError):
        smartphone_1 + lawngrass_1


def test_product_mixin(capsys):
    Product(name="Холодильник", description="Холодильник LG", price=30000, quantity=5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Холодильник, Холодильник LG, 30000, 5)"


def test_smartphone_mixin(capsys):
    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"


def test_lawn_grass_mixin(capsys):
    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"


def test_order_init(product_3):
    order = Order(product_3, 10)
    assert order.products == 'Насос, Насос автомобильный "Силач 3000"'
    assert order.quantity == 10
    assert order.total_price == 40000


def test_order_new_quantity(product_3):
    order = Order(product_3, 10)
    assert order.products == 'Насос, Насос автомобильный "Силач 3000"'
    assert order.quantity == 10
    assert order.total_price == 40000
    order.quantity = 15
    assert order.products == 'Насос, Насос автомобильный "Силач 3000"'
    assert order.quantity == 25
    assert order.total_price == 100000


def test_order_new_product(product_3):
    order = Order(product_3, 10)
    assert order.products == 'Насос, Насос автомобильный "Силач 3000"'
    assert order.quantity == 10
    assert order.total_price == 40000
    with pytest.raises(ValueError):
        order.products = "New_product"
        