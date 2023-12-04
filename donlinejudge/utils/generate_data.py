from faker import Faker
from accounts.models import User
from problem.models import ProblemTag, Problem
from submission.models import Submission
import random
import json

fake = Faker()


def pick_random_admin_user():
    admin_id = User.objects.get(is_superuser=True)
    return admin_id


def pick_random_user():
    return User.objects.all().order_by("?")[:1]


def pick_random_problem():
    return Problem.objects.all().order_by("?")[:1]


def generate_user(num: int):
    for _ in range(num):
        user = User.objects.create(
            username=fake.user_name(), email=fake.email(), password="12345678"
        )
        user.save()


def generate_problem(num: int):
    DEFAULT_STATEMENT = "Takahashi wants a beverage called AtCoder Drink in a restaurant. It can be ordered at a regular price of P yen.\r\nHe also has a discount coupon that allows him to order it at a lower price of \r\nQ yen. However, he must additionally order one of the restaurant's \r\nN dishes to use that coupon. For each \r\ni=1,2,…,N, the price of the \r\ni-th dish is \r\nD i yen.\r\n\r\nPrint the minimum total amount of money that he must pay to get the drink.\r\nInput\r\nN P Q \r\nD 1 ​ D 2 ​ … D N ​\r\nOutput\r\nPrint the answer."
    DEFAULT_TAG = [{"id": 1, "tag_name": "uncategorized"}]
    DEFAULT_SAMPLE_TEST = [
        {"input": "3 100 50\n60 20 40\n", "output": "70"},
        {"input": "3 100 50\n60000 20000 40000\n", "output": "100"},
    ]
    DEFAULT_TEST_ZIP = "/media/tests/1.zip"

    for i in range(num):
        problem = Problem.objects.create(
            display_id=fake.uuid4(),
            created=fake.date_time(),
            is_visible=True,
            author=pick_random_admin_user(),
            title="Order Something Else " + str(i),
            statement=DEFAULT_STATEMENT,
            difficulty="Easy",
            source=None,
            sample_test=DEFAULT_SAMPLE_TEST,
            test_zip=DEFAULT_TEST_ZIP,
        )
        problem.save()


def generate_submission(num: int):
    DEFAULT_CONTENT = "N, P, Q = map(int, input().split())\nD = list(map(int, input().split()))\n\nprint(min(P, Q+min(D)))"
    LANG = ["PyPy3", "Python3", "Python2", "Java", "C", "Cpp"]
    VERDICTS = [
        "Accepted",
        "Wrong Answer",
        "Time Limit Exceeded",
        "Memory Limit Exceeded",
        "Runtime Error",
        "Compile Error",
        "System Error",
        "Rejected",
    ]

    for _ in range(num):
        randomUser = pick_random_user()
        print("random user", randomUser)
        randomProblem = pick_random_problem()
        print("random problem", randomProblem)
        submission = Submission.objects.create(
            author_id=randomUser.values("id"),
            content=DEFAULT_CONTENT,
            language=random.choice(LANG),
            memory=random.randint(256, 1024),
            problem_id=randomProblem.values("id"),
            submit_time=fake.date_time(),
            time=random.randint(20, 20000),
            verdict=random.choice(VERDICTS),
        )

        submission.save()


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
