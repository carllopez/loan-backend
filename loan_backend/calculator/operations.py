from math import sqrt
from .random_string import generate_random_string


def addition(a, b):
    try:
        return a + b
    except TypeError as e:
        return None, str(e)

def subtract(a, b):
    try:
        return a - b
    except TypeError as e:
        return None, str(e)

def multiplication(a, b):
    if type(a) == str or type(b) == str:
        return None, "Multipliying strings is not allowed at the moment."
    return a * b

def division(a, b):
    try:
        return a / b
    except TypeError as e:
        return None, str(e)

def square_root(a):
    try:
        return sqrt(a)
    except TypeError as e:
        return None, str(e)

def random_string():
    return generate_random_string()
