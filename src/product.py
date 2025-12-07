from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity}"

    def __add__(self, other):
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, new_product_data: dict):

        name = new_product_data["name"]
        description = new_product_data["description"]
        price = new_product_data["price"]
        quantity = new_product_data["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            self.__price = self.__price
            print("Цена не должна быть нулевая или отрицательная")
            return

        if 0 < new_price < self.__price:
            answer = input("Новая цена меньше существующей, вы согласны изменить? (y/n)")
            if answer.lower() == "y":
                self.__price = new_price
            else:
                self.__price = self.__price
                print("Цена осталась прежней")
        else:
            self.__price = new_price
