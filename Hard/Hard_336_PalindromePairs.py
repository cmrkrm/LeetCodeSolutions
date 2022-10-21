class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pairs = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i==j: continue
                if ((words[i]+words[j]) == (words[i]+words[j])[::-1]):
                    pairs.append([i,j])
        return pairs