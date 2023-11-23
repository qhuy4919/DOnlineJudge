from faker import Faker
from accounts.models import User
from problem.models import ProblemTag
import random
import json

fake = Faker()


def generate_user(num: int):
    for _ in range(num):
        user = User.objects.create(
            username=fake.user_name(), email=fake.email(), password="12345678"
        )
        user.save()


def generate_tag():
    # Opening JSON file
    f = open(
        r"/home/qhuy/Desktop/dev/DOnlineJudge/donlinejudge/generate_data/management/resource/tag.json",
        "r",
    )
    data = json.load(f)
    for entry in data["data"]:
        problemTag = ProblemTag.objects.create(tag_name=entry["name"])
        problemTag.save()
