# Find the factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Example usage
if __name__ == "__main__":
    num = 5
    print(f"The factorial of {num} is {factorial(num)}")  # Output: 120

#  manual iterative approach to find factorial of a number
# def factorial_iterative(n):
#     if n < 0:
#         return "Factorial not defined for negative numbers"
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         fact = 1
#         for i in range(1, n + 1):
#             fact *= i # Multiply fact by each number from 1 to n
#         return fact

# number = 5
# print(f"The factorial of {number} is {factorial_iterative(number)}")

# Output: The factorial of 5 is 120
