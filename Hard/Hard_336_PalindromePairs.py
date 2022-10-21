class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pairs = []
        for i in range(len(words)):
            for j in range(i+1):
                if i==j: continue
                if ((words[i]+words[j]) == (words[i]+words[j])[::-1]): pairs.append([i,j])
                if ((words[j]+words[i]) == (words[j]+words[i])[::-1]): pairs.append([j,i])
        return pairs