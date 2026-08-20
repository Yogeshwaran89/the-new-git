# Sample Python Code

def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}! Welcome to the program."

def calculate_sum(numbers):
    """Calculate the sum of a list of numbers"""
    return sum(numbers)

def main():
    """Main function to demonstrate the program"""
    print("=== Welcome to Sample Program ===\n")
def factorial(n):

    """Calculate the factorial of a number"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")      
    fact =1
    for i in range(1, n + 1):
        fact *= i
    
    return fact

    # Example 1: Greet a user
    user_name = input("Enter your name: ")
    print(greet(user_name))
    
    # Example 2: Calculate sum
    numbers = [10, 20, 30, 40, 50]
    total = calculate_sum(numbers)
    print(f"\nSum of {numbers} is: {total}")
    
    # Example 3: Loop through items
    print("\n=== Looping through items ===")
    for i, num in enumerate(numbers, 1):
        print(f"Item {i}: {num}")
    
    # Example 4: Calculate factorial
    print("\n=== Factorial Calculation ===")
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        result = factorial(num)
        print(f"Factorial of {num} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    main()
