# Find common elements in two lists

def common_elements(list1, list2):
    # Convert the second list to a set for O(1) lookups
    set_list2 = set(list2)
    
    # Use a list comprehension to find common elements
    common = [element for element in list1 if element in set_list2]
    
    return common
# Example usage
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    print(common_elements(list1, list2))  # Output: [4, 5]




# other way to find common elements in two lists
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# common = list(set(list1) & set(list2))
# # Output: [3, 4]
