# Check if a string is a palindrome

def is_palindrome(s: str) -> bool:
    # Remove spaces and convert to lowercase
    cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]
# Example usage
if __name__ == "__main__":
    test_string = "A man, a plan, a canal: Panama"
    print(is_palindrome(test_string))  # Output: True