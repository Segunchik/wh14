import pytest

from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_product(product_1):
    assert product_1.name == "product name 1"
    assert product_1.description == "product description 1"
    assert product_1.price == 91.5
    assert product_1.quantity == 4


test_data = [
    {"name": "Товар 1", "description": "Описание товара 1", "price": 100.0, "quantity": 5, "expected_price": 100.0},
    {"name": "Товар 2", "description": "Описание товара 2", "price": 200.0, "quantity": 10, "expected_price": 200.0},
]


def test_class_method():
    for data in test_data:
        product_data = {
            "name": data["name"],
            "description": data["description"],
            "price": data["price"],
            "quantity": data["quantity"],
        }

        product = Product.new_product(product_data)

        assert product.name == data["name"]
        assert product.description == data["description"]
        assert product.price == data["expected_price"]
        assert product.quantity == data["quantity"]


def test_set_higher_price():
    product = Product("Товар", "Описание", 100, 5)
    product.price = 150
    print(product.price)
    assert product.price == 150


def test_set_lower_price():
    product = Product("Товар", "Описание", 100, 5)

    from unittest.mock import patch

    with patch("builtins.input", return_value="y"):
        product.price = 80
        assert product.price == 80

    with patch("builtins.input", return_value="n"):
        product.price = 70
        assert product.price == 80  # Цена не должна измениться
    print("Тест уменьшения цены пройден")


def test_product_str(product_1):
    assert str(product_1) == "product name 1, 91.5 руб. Остаток: 4"


def test_product_add(product_1, product_2):
    assert product_1 + product_2 == 670.5


def test_print_mixin(capsys):
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )

    message_1 = capsys.readouterr()
    assert (
        message_1.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    )

    LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    message_2 = capsys.readouterr()
    assert message_2.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"


def test_zero_quantity():
    with pytest.raises(ValueError) as excinfo:
        Product("name 1", "product description 1", 91.5, 0)

    assert str(excinfo.value) == "Товар с нулевым количеством не может быть добавлен"
