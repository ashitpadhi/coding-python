# Q: find start and end index of a number in a sorted list
# Ex: arr = [10,11,11,11,12,14]; output = [1,3]

from typing import List

class Solution:
    def startIndex(self, nums, target):
        left = 0; right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if (nums[mid]==target):
                if (mid-1>=0 and nums[mid-1]!=target or mid==0):
                    return mid
                right = mid-1
            elif (nums[mid] > target):
                right = mid-1
            else:
                left = mid+1
        return -1
    
    def endIndex(self, nums, target):
        left = 0; right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if (nums[mid]==target):
                if (mid+1<len(nums) and nums[mid+1]!=target or mid==len(nums)-1):
                    return mid
                left = mid+1
            elif (nums[mid] > target):
                right = mid-1
            else:
                left = mid+1
        return -1
    
    def searchRange(self, nums:List[int], target:int) -> List[int]:
        start = self.startIndex(nums, target)
        end = self.endIndex(nums, target)
        
        return [start, end]
    
# Test
output = Solution()
print(output.searchRange([10,11,11,11,14,15], 11))