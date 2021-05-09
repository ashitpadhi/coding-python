# Q: Valid mountain array problem
# if an array is increasing then decreasing
# Question from LeetCode 

from typing import List

class Solution:
    def ValidMountainArray(self, A:List[int]) -> bool:
        if len(A)<3:
            return False
        i = 0
        while (i<len(A) and A[i]>A[i-1]):
            i+=1
        if (i==1 or i==len(A)):
            return False
        while (i<len(A) and A[i]<A[i-1]):
            i+=1
        return i==len(A)


# Test
arr = [3,5,6,4,2]
isMountainArray = Solution()
isMountainArray.ValidMountainArray(arr)