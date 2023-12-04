from django.core.management.base import BaseCommand
from utils.generate_data import (
    generate_user,
    generate_tag,
    generate_problem,
    generate_submission,
)


class Command(BaseCommand):
    help = "Create sample data"

    def handle(self, *arg, **kwargs):
        # generate_user(100)
        # generate_tag()
        # generate_problem(10)
        generate_submission(20)
        print("complete!!!")
