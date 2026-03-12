def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b

def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a % b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid input! Please enter a number.\n")

def main():
    print("=" * 40)
    print("        SIMPLE CALCULATOR")
    print("=" * 40)

    while True:
        print("\nSelect an operation:")
        print("  1. Addition       (+)")
        print("  2. Subtraction    (-)")
        print("  3. Multiplication (*)")
        print("  4. Division       (/)")
        print("  5. Modulus        (%)")
        print("  6. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "6":
            print("\nThank you for using the calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("  Invalid choice! Please enter a number between 1 and 6.")
            continue

        a = get_number("Enter first number:  ")
        b = get_number("Enter second number: ")

        try:
            if choice == "1":
                result = add(a, b)
                op = "+"
            elif choice == "2":
                result = subtract(a, b)
                op = "-"
            elif choice == "3":
                result = multiply(a, b)
                op = "*"
            elif choice == "4":
                result = divide(a, b)
                op = "/"
            elif choice == "5":
                result = modulus(a, b)
                op = "%"

            print(f"\n  Result: {a} {op} {b} = {result}")

        except ZeroDivisionError as e:
            print(f"\n  Error: {e}")

if __name__ == "__main__":
    main()
