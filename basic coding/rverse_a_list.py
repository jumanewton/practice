# Reverse a list

def reverse_list(lst):
    # Method 1: Using slicing
    return lst[::-1]

    # Method 2: Using the built-in reverse() method (in-place)
    # lst.reverse()
    # return lst

    # Method 3: Using a loop to create a new reversed list
    # reversed_lst = []
    # for item in lst:
    #     reversed_lst.insert(0, item)  # Insert at the beginning
    # return reversed_lst

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print(reverse_list(my_list))  # Output: [5, 4, 3, 2, 1]


# short and efficient way to reverse a list
# my_list = [1, 2, 3, 4]
# my_list.reverse()
# print(my_list)  # Output: [4, 3, 2, 1]
