from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) 
        for word in strs: 
            count = []
            for i in range(26): 
                count.append(0)
            
            for character in word: 
                count[ord(character) - ord("a")] += 1 

            result[tuple(count)].append(word)

        return list(result.values())
                