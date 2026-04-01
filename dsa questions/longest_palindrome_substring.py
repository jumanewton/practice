# Find the longest palindromic substring
def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd length palindromes
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        
        # Even length palindromes
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
            
    return longest
# Example usage
if __name__ == "__main__":
    test_string = "babad"
    print(longest_palindrome(test_string))  # Output: "aba" or "bab"

# def longestPalindrome(s: str) -> str:
#     if not s or len(s) < 1:
#         return ""
    
#     start, end = 0, 0
    
#     # Helper function to expand outward
#     def expandAroundCenter(left: int, right: int) -> int:
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         # Returns length of the palindrome found
#         return right - left - 1

#     for i in range(len(s)):
#         # Case 1: Odd length palindrome (e.g., "racecar", center is 'e')
#         len1 = expandAroundCenter(i, i)
#         # Case 2: Even length palindrome (e.g., "abba", center is 'b'|'b')
#         len2 = expandAroundCenter(i, i + 1)
        
#         max_len = max(len1, len2)
        
#         # Update start and end pointers if a longer palindrome is found
#         if max_len > end - start:
#             start = i - (max_len - 1) // 2
#             end = i + max_len // 2
            
#     return s[start:end + 1]

# # Example Usage
# print(longestPalindrome("babad")) # Output: "bab" or "aba"
# print(longestPalindrome("cbbd"))  # Output: "bb"
