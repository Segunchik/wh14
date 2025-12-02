from src.product import Product


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
