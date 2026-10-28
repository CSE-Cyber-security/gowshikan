"""A simple command-line calculator."""

def calculate(first, operator, second):
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first / second
    raise ValueError("Unsupported operator. Use +, -, *, or /.")


def main():
    print("Simple Calculator")
    print("Operators: +, -, *, /")
    try:
        first = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ").strip()
        second = float(input("Enter the second number: "))
        result = calculate(first, operator, second)
        print(f"Result: {result:g}")
    except ValueError as error:
        print(f"Input error: {error}")
    except ZeroDivisionError as error:
        print(f"Calculation error: {error}")


if __name__ == "__main__":
    main()
