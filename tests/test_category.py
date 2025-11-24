def test_category(category_1, category_2):
    assert category_1.name == "category name1"
    assert category_1.description == "description1"
    assert len(category_1.products) == 3

    assert category_2.name == "category name2"
    assert category_2.description == "description2"
    assert len(category_2.products) == 2

    assert category_1.category_count == 2
    assert category_1.product_count == 5

    assert category_2.category_count == 2
    assert category_2.product_count == 5
