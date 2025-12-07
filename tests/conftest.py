import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def category_1():
    return Category(
        name="category name1",
        description="description1",
        products=[
            Product("product name 1", "product description 1", 31.5, 8),
            Product("product name 2", "product description 2", 41.5, 7),
            Product("product name 3", "product description 3", 51.5, 6),
        ],
    )


@pytest.fixture
def category_2():
    return Category(
        name="category name2",
        description="description2",
        products=[
            Product("product name 4", "product description 4", 61.5, 5),
            Product("product name 5", "product description 5", 71.5, 4),
        ],
    )


@pytest.fixture
def category_3():
    return Category(
        name="category name3",
        description="description3",
        products=[
            Product("product name 7", "product description 7", 161.5, 15),
            Product("product name 8", "product description 8", 171.5, 14),
        ],
    )


@pytest.fixture
def product_1():
    return Product("product name 1", "product description 1", 91.5, 4)


@pytest.fixture
def product_2():
    return Product("product name 6", "product description 6", 101.5, 3)


@pytest.fixture
def smartphone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone_2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawngrass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
