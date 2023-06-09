from faker import Faker
import random
from models import *
"""
fake = Faker()

users_pw = []

for _ in range(10):
    user_pw = User_Pw(
        username=fake.user_name(),
        email=fake.email() if random.choice([True, False]) else None,
        name=fake.name() if random.choice([True, False]) else None,
        disabled=random.choice([True, False]) if random.choice([True, False]) else None,
        hashed_password=fake.password()
    )
    users_pw.append(user_pw)
"""
def make_fake_users(n)-> list:
    fake = Faker()
    users_list =[]
    for _ in range(n):
        user_pw = User_Pw(
            username=fake.user_name(),
            email=fake.email() if random.choice([True, False]) else None,
            name=fake.name() if random.choice([True, False]) else None,
            disabled=random.choice([True, False]) if random.choice([True, False]) else None,
            hashed_password=fake.password()
    )
        users_list.append(user_pw)
    return users_list