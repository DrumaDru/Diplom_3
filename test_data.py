import random

curl = "https://stellarburgers.nomoreparties.site"

random_str = str(random.randint(1000, 9999))
payload = {
            "email": f"test_user{random_str}@yandex.ru",
            "password": 123456,
            "name": "test_user"
        }