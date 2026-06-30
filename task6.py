

# 1️⃣ Voting Eligibility Program
def check_voting_eligibility():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

# 2️⃣ Grade to Letter Conversion Function
def get_letter_grade():
    grade = float(input("Enter your grade percentage: "))
    if 90 <= grade <= 100:
        print("Your letter grade is: A")
    elif 80 <= grade < 90:
        print("Your letter grade is: B")
    elif 70 <= grade < 80:
        print("Your letter grade is: C")
    elif 60 <= grade < 70:
        print("Your letter grade is: D")
    else:
        print("Your letter grade is: F")

# 3️⃣ Simple Calculator
def calculator():
    print("Select operation: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice.")

# 4️⃣ Odd or Even Random Number Guess
import random
def odd_even_guess():
    number = random.randint(1, 100)
    print("Random number generated:", number)
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

