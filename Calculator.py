
def show_operations():
    print("\nAvailable Operations:")
    print(" +  : Addition")
    print(" -  : Subtraction")
    print(" *  : Multiplication")
    print(" /  : Division")
    print(" %  : Modulo")
    print(" ** : Power")

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            print("Error: Cannot divide by zero.")
            return None
        return a / b
    elif operator == '%':
        if b == 0:
            print("Error: Cannot perform modulo by zero.")
            return None
        return a % b
    elif operator == '**':
        return a ** b
    else:
        print("Invalid operator.")
        return None

def main():
    print("Simple Python Calculator")
    
    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    show_operations()

    while True:
        op = input("\nSelect an operation: ")
        if op not in ['+', '-', '*', '/', '%', '**']:
            print("Invalid operator selected.")
            continue

        try:
            num2 = float(input("Enter next number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        result = calculate(num1, num2, op)
        if result is not None:
            print(f"Result: {num1} {op} {num2} = {result}")
            choice = input("Do you want to continue with this result? (y/n): ").lower()
            if choice == 'y':
                num1 = result
            else:
                print("\nThank you for using the calculator. Bye!\n")
                break
        else:
            print("Calculation failed due to an error. Try again.")


if __name__ == "__main__":
    main()
