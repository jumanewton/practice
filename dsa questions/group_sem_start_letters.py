# Group strings by same starting letter
def group_by_start_letter(strings):
    groups = {}
    
    for s in strings:
        if s:  # Check if the string is not empty
            first_letter = s[0].lower()  # Use lower() to group case-insensitively
            if first_letter in groups:
                groups[first_letter].append(s)
            else:
                groups[first_letter] = [s]
    
    return groups
# Example usage
if __name__ == "__main__":
    test_strings = ["apple", "banana", "avocado", "grape", "blueberry", "apricot"]
    result = group_by_start_letter(test_strings)
    print(result)
    # Output: {'a': ['apple', 'avocado', 'apricot'], 'b': ['banana', 'blueberry'], 'g': ['grape']}

# Alternative approach using defaultdict
# from collections import defaultdict
# def group_by_start_letter(strings):
#     groups = defaultdict(list)
#     for s in strings:
#         if s:  # Check if the string is not empty
#             first_letter = s[0].lower()  # Use lower() to group case-insensitively
#             groups[first_letter].append(s)
#     return dict(groups)  # Convert back to a regular dictionary if desired
# Example usage
# if __name__ == "__main__":
#     test_strings = ["apple", "banana", "avocado", "grape", "blueberry", "apricot"]
#     result = group_by_start_letter(test_strings)
#     print(result)
#     # Output: {'a': ['apple', 'avocado', 'apricot'], 'b': ['banana', 'blueberry'], 'g': ['grape']}
