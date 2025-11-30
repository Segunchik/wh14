import pytest

from src.category import Category
from src.product import Product


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
