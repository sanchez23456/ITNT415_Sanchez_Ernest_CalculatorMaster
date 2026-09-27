def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide two numbers, handling division by zero."""
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b


def get_numbers():
    """Prompt the user for two numbers with input validation."""
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter numeric values only.\n")


def display_menu():
    print("\n===== Calculator Master =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid option. Please choose 1-5.\n")
            continue

        a, b = get_numbers()

        if choice == "1":
            print(f"Result: {add(a, b)}")
        elif choice == "2":
            print(f"Result: {subtract(a, b)}")
        elif choice == "3":
            print(f"Result: {multiply(a, b)}")
        elif choice == "4":
            print(f"Result: {divide(a, b)}")


if __name__ == "__main__":
    main()