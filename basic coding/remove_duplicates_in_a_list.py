# Remove duplicates from a list (maintain order)
def remove_duplicates(lst):
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 2, 4, 1, 5]
    print(remove_duplicates(my_list))  # Output: [1, 2, 3, 4, 5]



# my_list = ["apple", "banana", "apple", "orange", "banana"]
# unique_list = list(dict.fromkeys(my_list))
# # Output: ['apple', 'banana', 'orange']
