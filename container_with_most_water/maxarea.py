# Q: Find container with most water problem; finding the max size of rectangle in a bar chart


def maxArea(arr):
    maxarea = 0
    left = 0
    right = len(arr) -1
    
    while left<right:
        maxarea = max(maxarea, min(arr[left], arr[right])*(right-left))
        
        if arr[left]<arr[right]:
            left+=1
        else:
            right-=1
    return maxarea

arr1 = [1,8,6,2,5,4,8,3,7]
maxArea(arr1)