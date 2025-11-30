class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
            print("Цена не должна быть нулевая или отрицательная")

        if 0 < new_price < self.__price:
            answer = input("Новая цена меньше существующей, вы согласны изменить? (y/n)")
            if answer.lower() == "y":
                self.__price = new_price
            else:
                print("Цена осталась прежней")
