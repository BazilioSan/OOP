from src.product import Product, Category

from unittest.mock import patch


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
        "quantity": 15
    }
    product = Product.new_product(product_data)
    assert product.name == "Samsung Galaxy S21"
    assert product.description == "The latest Samsung flagship"
    assert product.price == 799.99
    assert product.quantity == 15


def test_product_price_change():
    with patch('builtins.input', return_value='y'):
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
