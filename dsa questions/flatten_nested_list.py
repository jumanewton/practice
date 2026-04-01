# Flatten a nested list (maintain order)
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))  # Recursively flatten the sublist
        else:
            flat_list.append(item)  # Append non-list items directly
    return flat_list
# Example usage
if __name__ == "__main__":
    nested_list = [1, [2, 3], [4, [5, 6]], 7]
    print(flatten(nested_list))  # Output: [1, 2, 3, 4, 5, 6, 7]

# other way to flatten a nested list using list comprehension
def flatten_comprehension(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_comprehension(item))  # Recursively flatten the sublist
        else:
            flat_list.append(item)  # Append non-list items directly
    return flat_list    
# Example usage
if __name__ == "__main__":
    nested_list = [1, [2, 3], [4, [5, 6]], 7]
    print(flatten_comprehension(nested_list))  # Output: [1, 2, 3, 4, 5, 6, 7]
    