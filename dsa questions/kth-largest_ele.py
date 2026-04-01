# Find the k-th largest element in a list
def kth_largest(nums, k):
    # Sort the list in descending order
    sorted_nums = sorted(nums, reverse=True)
    
    # Return the k-th largest element (k-1 index)
    return sorted_nums[k - 1]
# Example usage
if __name__ == "__main__":
    numbers = [3, 1, 4, 1, 5, 9]
    k = 3
    print(kth_largest(numbers, k))  # Output: 4



# Another way to find the k-th largest element using a min-heap
import heapq
def kth_largest_heap(nums, k):
    # Use a min-heap to keep track of the k largest elements
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)  # Remove the smallest element in the heap
    
    return min_heap[0]  # The root of the heap is the k-th largest element
# Example usage
if __name__ == "__main__":
    numbers = [3, 1, 4, 1, 5, 9]
    k = 3
    print(kth_largest_heap(numbers, k))  # Output: 4