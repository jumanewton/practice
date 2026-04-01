# Find the first non-repeating character in a string

def first_non_repeating_char(s):
    char_count = {}
    
    # Count the occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char
            
    return None  # Return None if there is no non-repeating character
# Example usage
if __name__ == "__main__":
    test_string = "swiss"
    result = first_non_repeating_char(test_string)
    if result:
        print(f"The first non-repeating character is: {result}")  # Output: w
    else:
        print("There is no non-repeating character.")

# alternative approach using collections.Counter
# from collections import Counter

# def first_unique_char(s):
#     counts = Counter(s)
#     for char in s:
#         if counts[char] == 1:
#             return char
#     return None  # Or return -1 or '$' if none found
# # Example usage
# if __name__ == "__main__":
#     test_string = "swiss"
#     result = first_unique_char(test_string)
#     if result:
#         print(f"The first non-repeating character is: {result}")  # Output: w
#     else:
#         print("There is no non-repeating character.")