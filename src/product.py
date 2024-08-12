class Product:
    """ "Класс описывающий отдельный продукт"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            user_answer = input("Подтвердите снижение цены. Введите y/n: ")
            if user_answer == "y":
                self.__price = new_price
            elif user_answer == "n":
                self.__price = self.__price
        elif new_price > self.__price:
            self.__price = new_price

    @classmethod
    def new_product(cls, kwargs):
        return Product(**kwargs)


class Category:
    """Класс описывающий категории продуктов"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price}. Остаток: {product.quantity}шт.\n"
        return products_str

    @property
    def products_list(self):
        return self.__products

    def add_product(self, product: Product):
        for item in self.__products:
            if item.name == product.name:
                item.quantity += product.quantity
                if item.price < product.price:
                    item.price = product.price
                return
        self.__products.append(product)
        Category.product_count += 1