# Q: Finding longest substring without repeating letters in a string


def longestSubstr(string):
    m = {}; left = 0; right = 0
    ans = 0
    n = len(string)
    while (left<n and right<n):
        el = string[right]
        if (el in m):
            left = max(left, m[el]+1)
        m[el] = right
        ans = max(ans, right-left+1)
        right+=1
    return ans

# Test
str_ = 'abacadb'
longestSubstr(str_)