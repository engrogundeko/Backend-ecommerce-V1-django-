import factory
import pytest
from faker import Faker
from pytest_factoryboy import register

fake = Faker()
from ecommerce.inventory import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = fake.lexify(text="cat_name_??????")
    slug = fake.lexify(text="cat_slug_??????")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    web_id = factory.Sequence(lambda n: "web_id_%d" % n)
    slug = fake.lexify(text="prod_slug_??????")
    name = fake.lexify(text="prod_name_??????")
    description = fake.text()
    is_active = True
    created_at = "2021-09-04 22:14:18.279092"
    updated_at = "2021-09-04 22:14:18.279092"

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not extracted or not create:
            return
        if extracted:
            for cat in extracted:
                self.category.add(cat)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Brand

    name = factory.Sequence(lambda n: "brand_%d" % n)


class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductType

    name = factory.Sequence(lambda n: "type_%d" % n)


class ProductInventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductInventory

    sku = factory.Sequence(lambda n: "web_id_%d" % n)
    upc = factory.Sequence(lambda n: "web_id_%d" % n)
    product_type = factory.SubFactory(ProductTypeFactory)
    product = factory.SubFactory(ProductFactory)
    # product_type = factory.SubFactory(ProductFactory)
    brand = factory.SubFactory(BrandFactory)
    is_active = True
    is_active = 1
    retail_price = 97
    store_price = 92
    sale_price = 46
    weight = 987

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not extracted or not create:
            return
        if extracted:
            for cat in extracted:
                self.category.add(cat)


class MediaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Media

    product_inventory = factory.SubFactory(ProductInventoryFactory)

    image = "images/default.png"
    alt_text = "a default image solid color"
    is_feature = True


class StockFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Stock

    product_inventory = factory.SubFactory(ProductInventoryFactory)
    units = 2
    units_sold = 100


class ProductAttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductAttribute

    name = "attribute_name_0"
    description = "attribute_description"

class ProductAttributeValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ProductAttributeValue

    product_attribute = factory.SubFactory(ProductAttributeFactory)
    attribute_value = "10"    

register(CategoryFactory)
register(ProductFactory)
register(ProductTypeFactory)
register(BrandFactory)
register(ProductInventoryFactory)
register(MediaFactory)
register(StockFactory)
register(ProductAttributeFactory)
register(ProductAttributeValueFactory)
