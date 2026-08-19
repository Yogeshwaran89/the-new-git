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

if __name__ == "__main__":
    main()
