# Find all anagrams in a list of words

def find_anagrams(words):
    anagram_dict = {}
    
    for word in words:
        # Sort the characters of the word to get the anagram key
        sorted_word = ''.join(sorted(word))
        
        # Add the original word to the list of anagrams for this key
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    
    # Filter out groups of anagrams that have more than one word
    return [group for group in anagram_dict.values() if len(group) > 1]
# Example usage
if __name__ == "__main__":
    words = ["listen", "silent", "enlist", "inlets", "google", "gooogle"]
    print(find_anagrams(words))  # Output: [['listen', 'silent', 'enlist', 'inlets']]

# other way to find anagrams in a list of words
# from collections import defaultdict

# def find_anagrams(word_list):
#     # Use defaultdict to automatically create a list for each new key
#     anagram_map = defaultdict(list)
    
#     for word in word_list:
#         # Sort characters to create a 'canonical' key (e.g., 'eat' -> 'aet')
#         sorted_key = "".join(sorted(word.lower()))
#         anagram_map[sorted_key].append(word)
    
#     # Return only the groups that have more than one word (actual anagrams)
#     return [group for group in anagram_map.values() if len(group) > 1]

# # Example usage
# words = ["eat", "tea", "tan", "ate", "nat", "bat", "listen", "silent"]
# print(find_anagrams(words))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['listen', 'silent']]
