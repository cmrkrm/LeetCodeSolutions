class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pairs = []
        for i in range(len(words)):
            for j in range(i+1):
                words_ij = words[i]+words[j]
                words_ji = words[j]+words[i]
                if (words_ij == words_ij[::-1]): pairs.append([i,j])
                if (words_ji == words_ji[::-1]): pairs.append([j,i])
        return pairs