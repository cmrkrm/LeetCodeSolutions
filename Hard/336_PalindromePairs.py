# You are given a 0-indexed array of unique strings words.

# A palindrome pair is a pair of integers (i, j) such that:

# 0 <= i, j < word.length,
# i != j, and
# words[i] + words[j] (the concatenation of the two strings) is a palindrome string.
# Return an array of all the palindrome pairs of words.

class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        locations = []
        for i in range (0, len(words) - 1):
            for j in range (i + 1, len(words)):
                new_word = words[i] + words[j]
                if new_word == new_word[::-1]:
                    locations.append([i,j])
                new_word = words[j] + words[i]
                if new_word == new_word[::-1]:
                    locations.append((j,i))             
        return locations