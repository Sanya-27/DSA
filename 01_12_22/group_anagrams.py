class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d= {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in d:
                d[sortedWord].append(word)
            else:
                d[sortedWord] = [word]
        return list(d.values())