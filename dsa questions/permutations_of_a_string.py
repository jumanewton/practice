# Generate all permutations of a string
def permute_string(s):
    if len(s) == 1:
        return [s]
    
    permutations = []
    for i, char in enumerate(s):
        # Get the remaining characters
        remaining = s[:i] + s[i+1:]
        # Generate permutations of the remaining characters
        for perm in permute_string(remaining):
            permutations.append(char + perm)
    
    return permutations
# Example usage
if __name__ == "__main__":
    test_string = "abc"
    print(permute_string(test_string))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']


# Alternative approach using itertools.permutations
from itertools import permutations

s = "ABC"
# Generate all permutations and join tuples back into strings
all_perms = [''.join(p) for p in permutations(s)]
print(all_perms)
# Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
