import pytest
from django.core.management import call_command
# from django.contrib.auth import get_user_model


# @pytest.fixture
# def create_admin_user():
#     User = get_user_model()
#     return User.objects.create_superuser("user", "user@gmail.com", "password")


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixtures.json")
        call_command("loaddata", "db_category_fixtures.json")
        call_command("loaddata", "db_product_fixtures.json")
        call_command("loaddata", "db_brand_fixtures.json")
        call_command("loaddata", "db_type_fixture.json")
        call_command("loaddata", "db_product_inventory.json")
        call_command("loaddata", "db_media_fixtures.json")
        call_command("loaddata", "db_stock_fixtures.json")
        call_command("loaddata", "db_product_attribute_fixtures.json")
        call_command("loaddata", "db_product_attribute_value.json")
