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

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

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

    def __str__(self):
        total_quantity = 0
        for item in self.__products:
            total_quantity += item.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products_list(self):
        return self.__products

    def add_product(self, product: Product):
        if isinstance(product, Product):
            for item in self.__products:
                if item.name == product.name:
                    item.quantity += product.quantity
                    if item.price < product.price:
                        item.price = product.price
                    return
        else:
            raise TypeError
        self.__products.append(product)
        Category.product_count += 1


class CatIterator:
    """Класс итератора, для перебора товара одной категории"""

    def __init__(self, cat_object):
        self.cat_object = cat_object
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.cat_object.products_list):
            prod = self.cat_object.products_list[self.index]
            self.index += 1
            return prod
        else:
            raise StopIteration


class LawnGrass(Product):
    """Класс описывает газонную траву. Родительский класс - Product"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)


class Smartphone(Product):
    """Класс описывает смартфоны. Родительский класс - Product"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)
