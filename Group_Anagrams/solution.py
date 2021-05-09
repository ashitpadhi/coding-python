
from typing import List
class Solution:
    
    def findHash(self, s):
        return ''.join(sorted(s))
    
    def groupAnamgrams(self, strs:List[str]) -> List[List[str]]:
        result = []
        m = {}
        
        for s in strs:
            sorted_s = self.findHash(s)
            if sorted_s not in m:
                m[sorted_s] = []
            m[sorted_s].append(s)
        
        for p in m.values():
            result.append(p)
        
        return result

# Test    
strs = ['tca','god','tac','dog','cat','man']
anagram = Solution()
anagram.groupAnamgrams(strs)


"""
# Solution2:

from itertools import groupby
words = sorted(words, key=sorted)
print(words)

print([list(group) for key,group in groupby(words, sorted)])

"""