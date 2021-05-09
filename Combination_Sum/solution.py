# Q: Combination Sum. 

from typing import List
class Solution:
    
    def solution(self, candidates, ans, cur, target, index, sum):
        if (sum==target):
            ans.append(cur)
        elif (sum<target):
            n = len(candidates)
            for i in range(index, n):
                cur.append(candidates[i])
                self.solution(candidates, ans, cur, target, i, (sum+candidates[i]))
                cur.pop()
            return            
    
    def combinationSum(self, candidates:List[int], target:int) -> List[List[int]]:
        ans = []
        cur = []
        self.solution(candidates, ans, cur, target, 0, 0)
        return ans

# Test    
candidates = [2,3,6,7]
target = 7
combsum = Solution()
# combsum.combinationSum(candidates, target)