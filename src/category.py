from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)


    def __str__(self):
        sum_products: int = 0
        for i in self.__products:
            sum_products += i.quantity
        return f"{self.name}, количество продуктов: {sum_products}"

    @property
    def products(self):
        return "".join(
            [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n" for product in self.__products]
        )

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1
