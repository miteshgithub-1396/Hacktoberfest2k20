# Define the calculator function
def calculator():
    print("Welcome to the Simple Calculator!")
    
    while True:
        # Menu for operations
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")
        
        # User input for operation choice
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        # Check if the choice is to quit
        if choice == '5':
            print("Goodbye!")
            break
        
        # Input validation
        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice. Please select a valid operation.")
            continue
        
        # Input for numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform the selected operation
        if choice == '1':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")

# Run the calculator function
calculator()
