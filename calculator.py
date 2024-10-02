class Calculator:
    def __init__(self):
        print("Calculator object created")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a // b  # Integer division in Python

    def modulo(self, a, b):
        return a % b

if __name__ == "__main__":
    calculator = Calculator()

    print("Addition:", calculator.add(10, 20))
    print("Subtraction:", calculator.subtract(10, 20))
    print("Multiplication:", calculator.multiply(10, 20))
    print("Division:", calculator.divide(10, 20))
    print("Modulo:", calculator.modulo(10, 7))
