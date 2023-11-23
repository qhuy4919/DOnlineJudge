from django.core.management.base import BaseCommand
from utils.generate_data import generate_user, generate_tag


class Command(BaseCommand):
    help = "Create sample data"

    def handle(self, *arg, **kwargs):
        # generate_user(10)
        # generate_tag()
        print("complete!!!")
