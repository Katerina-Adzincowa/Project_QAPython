import os
from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str
    password: str = os.getenv('BASE_PASSWORD', None)
    password_confirmation: str = os.getenv('BASE_PASSWORD', None)


BOB = User(name='bob_user', email='bob@example.com', password='password123')
NEWBOB = User(name='NewBob', email='newbob@gmail.com', password='password123', password_confirmation='password123')
