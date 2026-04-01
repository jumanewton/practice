# Merge two sorted lists (result must remain sorted)
import heapq

list1 = [1, 3, 5]
list2 = [2, 4, 6]

merged_list = list(heapq.merge(list1, list2))

print(merged_list)
# Output: [1, 2, 3, 4, 5, 6]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
#     # Create a dummy node to simplify the logic
#     dummy = ListNode()
#     current = dummy

#     # Traverse both lists and merge them
#     while l1 and l2:
#         if l1.val < l2.val:
#             current.next = l1
#             l1 = l1.next
#         else:
#             current.next = l2
#             l2 = l2.next
#         current = current.next

#     # Attach any remaining nodes from either list
#     current.next = l1 or l2

#     # Return the merged list (skip the dummy node)
#     return dummy.next


# algorithimic way to merge two sorted lists (manual iterative approach)
# def merge_sorted_lists(list1, list2):
#     merged_list = []
#     i = 0  # Pointer for list1
#     j = 0  # Pointer for list2

#     # Traverse both lists and append the smaller element
#     while i < len(list1) and j < len(list2):
#         if list1[i] <= list2[j]:
#             merged_list.append(list1[i])
#             i += 1
#         else:
#             merged_list.append(list2[j])
#             j += 1

#     # Append remaining elements from list1 (if any)
#     if i < len(list1):
#         merged_list.extend(list1[i:])

#     # Append remaining elements from list2 (if any)
#     if j < len(list2):
#         merged_list.extend(list2[j:])

#     return merged_list

# list1 = [1, 5, 9]
# list2 = [2, 6, 10]
# merged_list = merge_sorted_lists(list1, list2)

# print(merged_list)
# # Output: [1, 2, 5, 6, 9, 10]
