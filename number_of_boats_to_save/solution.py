# Q: number of boats required to save all people in an array
# Question from LeetCode 

def numRescureBoats(arr, limit):
    arr.sort()
    left = 0; right = len(arr) -1
    boats_number = 0
    
    while (left <= right):
        if (left == right):
            boats_number +=1
            break
        if (arr[left]+arr[right] <= limit):
            left += 1
        right -= 1
        boats_number +=1
    return boats_number

# Test
arr = [3,4,5,2,3]
limit= 5
print(numRescureBoats(arr, limit))