# Find the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
if __name__ == "__main__": 
    num1 = 48
    num2 = 18
    print(gcd(num1, num2))  # Output: 6