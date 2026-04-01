# Count vowels in a string

def count_vowels(s: str) -> int:
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
# Example usage
if __name__ == "__main__":
    test_string = "Hello World!"
    print(count_vowels(test_string))  # Output: 3