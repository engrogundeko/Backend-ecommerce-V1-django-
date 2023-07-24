import pytest

from ecommerce.inventory import models


@pytest.mark.dbfixtures
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (17, "golf", "golf", 1),
        (23, "contemporary", "contemporary", 0),
        (35, "baseball", "baseball", 1),
        (29, "eco-friendly", "eco-friendly", 1),
    ]
)
def test_inventory_category_dbfixtures(
    db, django_db_setup, id, name, slug, is_active
):
    results = models.Category.objects.get(id=id)
    assert results.name == name
    assert results.slug == slug
    assert results.is_active == is_active

@pytest.mark.dbfixtures
@pytest.mark.parametrize(
    "name, slug, is_active",
    [
        ("fashion", "fashion", 1),
        ("shoes", "shoes", 0),
        ("django", "django", 1),
        ("games", "games", 0),
    ]
)
def test_inventory_category_insert_data(
    db, category_factory, name, slug, is_active
):
    results = category_factory.create(name=name, slug=slug, is_active=is_active)
    assert results.name == name
    assert results.slug == slug
    assert results.is_active == is_active
