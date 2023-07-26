import pytest
from django.db import IntegrityError

from ecommerce.inventory import models


@pytest.mark.dbfixtures
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (17, "golf", "golf", 1),
        (23, "contemporary", "contemporary", 0),
        (35, "baseball", "baseball", 1),
        (29, "eco-friendly", "eco-friendly", 1),
    ],
)
def test_inventory_category_dbfixtures(db, django_db_setup, id, name, slug, is_active):
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
    ],
)
def test_inventory_category_insert_data(db, category_factory, name, slug, is_active):
    results = category_factory.create(name=name, slug=slug, is_active=is_active)
    assert results.name == name
    assert results.slug == slug
    assert results.is_active == is_active


@pytest.mark.dbfixtures
@pytest.mark.parametrize(
    "id, web_id, name, slug, description, is_active, created_at, updated_at",
    [
        (
            1,
            "45425810",
            "widstar running sneakers",
            "widstar-running-sneakers",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            8616,
            "45434425",
            "impact puse dance shoe",
            "impact-puse-dance-shoe",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_product_dbfixtures(
    db,
    django_db_setup,
    id,
    web_id,
    slug,
    name,
    description,
    is_active,
    created_at,
    updated_at,
):
    results = models.Product.objects.get(id=id)

    results_created_at = results.created_at.strftime("%Y-%m-%d %H:%M:%S")
    results_updated_at = results.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    assert results.web_id == web_id
    assert results.slug == slug
    assert results.name == name
    assert results.description == description
    assert results.is_active == is_active
    assert results_created_at == created_at
    assert results_updated_at == updated_at


def test_inventory_product_uniqueness_integrity(db, product_factory):
    new_web_id = product_factory.create(web_id=123456789)
    with pytest.raises(IntegrityError):
        product_factory.create(web_id=123456789)


@pytest.mark.dbfixtures
def test_inventory_product_insert_data(db, product_factory, category_factory):
    # category_1 = category_factory.create()
    # category_2 = category_factory.create()
    new_product = product_factory.create(category=(1, 2, 3, 4, 5))

    result_product_category = new_product.category.all().count()

    assert "web_id" in new_product.web_id
    assert result_product_category == 5


@pytest.mark.dbfixtures
@pytest.mark.parametrize(
    "id, sku, upc, product_type, product, brand, is_active, retail_price, store_price, sale_price, weight, created_at, updated_at",
    [
        (
            1,
            "7633969397",
            "934093051374",
            1,
            1,
            1,
            1,
            97.00,
            92.00,
            46.00,
            987,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            8616,
            "3880741573",
            "844935525855",
            1,
            8616,
            1253,
            1,
            89.00,
            84.00,
            42.00,
            929,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_product_inventory_dbfixtures(
    db,
    django_db_setup,
    id,
    sku,
    upc,
    product_type,
    product,
    brand,
    is_active,
    retail_price,
    store_price,
    sale_price,
    weight,
    created_at,
    updated_at,
):
    results = models.ProductInventory.objects.get(id=id)

    results_created_at = results.created_at.strftime("%Y-%m-%d %H:%M:%S")
    results_updated_at = results.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    assert results.sku == sku
    assert results.upc == upc
    assert results.product_type.id == product_type
    assert results.product.id == product
    assert results.brand.id == brand
    assert results.is_active == is_active
    assert results.retail_price == retail_price
    assert results.store_price == store_price
    assert results.sale_price == sale_price
    assert results.weight == weight
    assert results_created_at == created_at
    assert results_updated_at == updated_at


@pytest.mark.dbfixtures
def test_inventory_productinventory_insert_data(
    db, django_db_setup, product_inventory_factory
):
    new_product_inventory = product_inventory_factory.create(
        sku="123456789",
        upc="123456789",
        product_type__name="new-name",
        product__web_id="123456789",
        brand__name="new-name",
    )
    assert new_product_inventory.sku == "123456789"
    assert new_product_inventory.upc == "123456789"
    assert new_product_inventory.product_type.name == "new-name"
    assert new_product_inventory.product.web_id == "123456789"
    assert new_product_inventory.brand.name == "new-name"
    assert new_product_inventory.is_active == 1
    assert new_product_inventory.retail_price == 97.00
    assert new_product_inventory.store_price == 92.00
    assert new_product_inventory.sale_price == 46.00
    assert new_product_inventory.weight == 987

@pytest.mark.dbfixtures
@pytest.mark.parametrize(
    "id, product_inventory, image, alt_text, is_feature, created_at, updated_at",
    [
        (
            1,
            1,
            "images/default.png",
            "a default image solid color",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            8616,
            8616,
            "images/default.png",
            "a default image solid color",
            1,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ]
)
def test_inventory_image_dbfixtures(
    db,
    django_db_setup,
    id,
    product_inventory,
    image, 
    alt_text, 
    is_feature, 
    created_at, 
    updated_at
):
    results = models.Media.objects.get(id=id)
    results_created_at = results.created_at.strftime("%Y-%m-%d %H:%M:%S")
    results_updated_at = results.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    assert results.product_inventory.id == product_inventory
    assert results.image == image
    assert results.alt_text == alt_text
    assert results.is_feature == is_feature
    assert results_created_at == created_at
    assert results_updated_at == updated_at


def test_inventory_image_insert_data(db, media_factory):
    new_image = media_factory.create(product_inventory__sku="123456789")

    assert new_image.product_inventory.sku == "123456789"
    assert new_image.image == "images/default.png"
    assert new_image.alt_text == "a default image solid color"
    assert new_image.is_feature == 1

@pytest.mark.dbfixtures
@pytest.mark.parametrize(
    "id, product_inventory, last_checked,units, units_sold", [
        (1, 1, "2021-09-04 22:14:18", 135, 0,),
        (8616, 8616, "2021-09-04 22:14:18", 100, 0),
    ]
)
def test_inventory_stock_dbfixtures(
    db,
    django_db_setup,
    id,
    product_inventory, 
    last_checked,
    units, 
    units_sold):
    results = models.Stock.objects.get(id=id)
    results_last_checked = results.last_checked.strftime("%Y-%m-%d %H:%M:%S")

    assert results.product_inventory.id == product_inventory
    assert results_last_checked == results_last_checked
    assert results.units == units
    assert results.units_sold == units_sold

def test_inventory_stock_insert_data(db, stock_factory):
    new_stock = stock_factory.create(product_inventory__sku="123456789")

    assert new_stock.product_inventory.sku == "123456789"
    assert new_stock.units == 2
    assert new_stock.units_sold == 100

@pytest.mark.dbfixtures
@pytest.mark.parametrize(
    "id, name, description,", [
        (1, "men-shoe-size", "men shoe size"),
    ]
)
def test_inventory_productattribute_dbfixtures(
    db, django_db_setup, id, name, description
):
    results = models.ProductAttribute.objects.get(id=id)

    assert results.name == name
    assert results.description == description


def test_iventory_productattribute_insert_data(
    db, product_attribute_factory
):
    new_productattribute = product_attribute_factory.create()

    assert product_attribute_factory.name == "attribute_name_0"
    assert product_attribute_factory.description == "attribute_description"

def test_inventory_productinventory_uniqueness(
        db, product_attribute_factory
):
    product_attribute_factory.create(name="not unique")
    with pytest.raises(IntegrityError):
        product_attribute_factory.create(name="not unique")


@pytest.mark.dbfixtures
@pytest.mark.parametrize(
    "id, product_attribute, attriubute_value,",
    [
        (1, 1, 10),
    ]
)
def test_inventory_product_attribute_value_dbfixtures(
    db, django_db_setup,id, product_attribute, attriubute_value, 
):
    results = models.ProductAttributeValue.objects.get(id=id)

    assert results.product_attribute.id == 1
    assert results.attribute_value == "10"

def test_inventory_product_attribute_insert_data(
        db, product_attribute_value_factory
):
    new_product_attribute_value = product_attribute_value_factory.create(
        product_attribute__name="new_value",
    )
    assert new_product_attribute_value.product_attribute.name == "new_value"
    assert new_product_attribute_value.attribute_value == "10"