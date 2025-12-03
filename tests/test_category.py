from src.category import Category
from src.product import Product


def test_category(category_1, category_2):
    assert category_1.name == "category name1"
    assert category_1.description == "description1"
    # assert len(category_1.products) == 3

    assert category_2.name == "category name2"
    assert category_2.description == "description2"
    # assert len(category_2.products) == 2

    assert category_1.category_count == 2
    assert category_1.product_count == 5

    assert category_2.category_count == 2
    assert category_2.product_count == 5


def test_add_product(category_3, product_2):
    category_3.add_product(product_2)
    # assert len(category_3.products) == 3
    assert Category.product_count == 8


def test_product_counters():
    # Создаем категорию и продукты
    category = Category(name="Электроника", description="Товары из категории электроники", products=[])

    product1 = Product(name="Смартфон", description="Современный смартфон", price=29999.99, quantity=10)

    product2 = Product(name="Ноутбук", description="Игровой ноутбук", price=99999.99, quantity=5)

    # Добавляем продукты и проверяем счетчик
    category.add_product(product1)
    category.add_product(product2)
    assert Category.product_count == 10


def test_category_str(category_2):
    assert str(category_2) == "category name2, количество продуктов: 9"
