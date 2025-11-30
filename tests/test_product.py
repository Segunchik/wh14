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
