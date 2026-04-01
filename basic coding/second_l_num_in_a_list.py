# Find the second largest element in a list
def find_second_largest(numbers):
    # Convert to a set to remove duplicates, then back to a list
    unique_numbers = list(set(numbers))

    # Check if there are at least two unique elements
    if len(unique_numbers) < 2:
        return None # Or handle the case as needed

    # Sort the unique list in ascending order
    unique_numbers.sort()

    # The second largest is at the second-to-last position (index -2)
    return unique_numbers[-2]

# Example usage:
my_list = [10, 20, 4, 45, 99, 99, 50]
second_largest = find_second_largest(my_list)
print(f"The second largest element is: {second_largest}")








# def second_largest(nums):
#     if len(nums) < 2:
#         return "List must contain at least two elements"
    
#     first = second = float('-inf')  # Initialize to negative infinity

#     for num in nums:
#         if num > first:
#             second = first  # Update second before updating first
#             first = num
#         elif first > num > second:  # Check if num is between first and second
#             second = num

#     return second if second != float('-inf') else "No second largest element"
# # Example usage
# if __name__ == "__main__":
#     numbers = [3, 1, 4, 1, 5, 9]
#     print(second_largest(numbers))  # Output: 5