from django.core.management.base import BaseCommand
from utils.generate_data import generate_user, generate_tag, generate_problem


class Command(BaseCommand):
    help = "Create sample data"

    def handle(self, *arg, **kwargs):
        # generate_user(100)
        # generate_tag()
        generate_problem(10)
        print("complete!!!")
