class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def operate(self, operation: str):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'subtract':
            return self.a - self.b
        elif operation == 'multiply':
            return self.a * self.b
        elif operation == 'divide':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Division by zero error"
        else:
            return "Invalid operation"

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()
    calc = Calculator(a, b)
    print("Result:", calc.operate(operation))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
