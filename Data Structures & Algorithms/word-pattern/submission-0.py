class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):          # Number of characters and words must be the same
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern,words):
            
            # Character already mapped to a different word
            if char in char_to_word and char_to_word[char] != word:
                return False

            # Word already mapped to a different character
            if word in word_to_char and word_to_char[word] != char:
                return False

            # Create the mapping
            char_to_word[char] = word
            word_to_char[word] = char
        return True