# calculator.py
from utils import add

def add(a, b):
    return a + b
#handling zero error

def divide(a, b):
    if b == 0:
        return None

    return a / b


if __name__ == "__main__":
    print(add(2, 3))
    print(divide(10, 2))
