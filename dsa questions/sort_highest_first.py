# Sort elements based on frequency (highest first, maintain order)
def sort_by_frequency(nums):
    from collections import Counter
    
    # Count the frequency of each element
    frequency = Counter(nums)
    
    # Sort the elements by frequency (highest first) and maintain original order for ties
    sorted_nums = sorted(nums, key=lambda x: (-frequency[x], nums.index(x)))
    
    return sorted_nums
# Example usage
if __name__ == "__main__":
    nums = [4, 5, 6, 5, 4, 3]
    print(sort_by_frequency(nums))  # Output: [4, 4, 5, 5, 6, 3]

# from collections import Counter
# counts = Counter(arr)
# # Stable sort preserves relative order for same frequencies
# arr.sort(key=lambda x: counts[x], reverse=True)
