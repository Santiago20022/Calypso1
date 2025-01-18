import random

# Function to perform a guessing game with numbers
def number_guessing_game():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

# Function to perform basic calculator operations
def calculator():
    print("\nWelcome to the calculator!")
    print("You can perform basic operations: addition, subtraction, multiplication, and division.")

    num1 = float(input("Enter the first number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "undefined (division by zero)"
    else:
        result = "Invalid operation"

    print(f"Result: {result}\n")

print("Welcome to the Number Guessing Game and Calculator!\n")

while True:
    # Display menu options
    print("Options:")
    print("1. Play the Number Guessing Game")
    print("2. Use the Calculator")
    print("3. Exit")

    # Get user's choice
    choice = input("Enter your choice (1, 2, or 3): ")

    # Match user's choice to the corresponding action
    match choice:
        case '1':
            # Call the number guessing game function
            number_guessing_game()

        case '2':
            # Call the calculator function
            calculator()

        case '3':
            # Exit the program
            print("Goodbye! Thanks for playing.")
            break

        case _:
            # Handle invalid input
            print("Invalid choice. Please try again.")
