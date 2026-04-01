# Find the missing number from 1 to n

def find_missing_number(nums):
    n = len(nums) + 1  # Since one number is missing, the total count should be n
    expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(nums)  # Sum of the given numbers
    return expected_sum - actual_sum  # The difference is the missing number
# Example usage
if __name__ == "__main__":
    nums = [1, 2, 4, 5]  # Missing number is 3
    print(find_missing_number(nums))  # Output: 3