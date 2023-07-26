from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command("makemigrations")
        call_command("migrate")
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
        
        # call_command("loaddata", "db_category_product_fixture.json")