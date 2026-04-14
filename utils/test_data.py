import random

def generate_employee_name():
    fname = "John" + str(random.randint(1000, 9999))
    lname = "Doe"
    return fname, lname


INVALID_LOGIN = {
    "username": "wronguser",
    "password": "wrongpass",
    "error": "Invalid credentials"
}