# Fibonacci sequence generator

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    print(f"Fibonacci sequence up to {n} numbers:")
    for num in fibonacci(n):
        print(num, end=' ')