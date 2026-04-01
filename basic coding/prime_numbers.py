# Generate prime numbers up to a given number n

import math

# def check_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True

# def generate_primes(n):
#     primes = []
#     for num in range(2, n + 1):
#         if check_prime(num):
#             primes.append(num)
#     return primes
# if __name__ == "__main__":
#     n = int(input("Enter a number: "))
#     primes = generate_primes(n)
#     print(f"Prime numbers up to {n}: {primes}")

# check if the number is prime or not
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
    # for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

number_to_check = 56
if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number")
else:
    print(f"{number_to_check} is not prime")
