from src.product import Product, Category


def test_product_creation():
    product = Product("iPhone 12", "Latest iPhone model", 999.99, 10)
    assert product.name == "iPhone 12"
    assert product.description == "Latest iPhone model"
    assert product.price == 999.99
    assert product.quantity == 10


def test_product_price_update():
    product = Product("iPhone 12", "Latest iPhone model", 999.99, 10)
    product.price = 1099.99
    assert product.price == 1099.99


def test_category_creation():
    product1 = Product("iPhone 12", "Latest iPhone model", 999.99, 10)
    product2 = Product("Samsung Galaxy S21", "Latest Samsung model", 899.99, 15)
    category = Category("Smartphones", "Latest smartphone models", [product1, product2])
    assert category.name == "Smartphones"
    assert category.description == "Latest smartphone models"
    assert len(category.products) == 2
    assert category.category_count == 1
    assert category.product_count == 2


def test_category_product_count():
    product1 = Product("iPhone 12", "Latest iPhone model", 999.99, 10)
    product2 = Product("Samsung Galaxy S21", "Latest Samsung model", 899.99, 15)
    category = Category("Smartphones", "Latest smartphone models", [product1, product2])
    assert category.product_count == 2
