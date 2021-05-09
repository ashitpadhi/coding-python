"""
Input: S = “abab”, T = “ab”
Output: abab
Explanation: The string “abab” is same as S and twice the concatenation of string T (“abab” = “ab” + “ab” = T + T)
"""


def findSmallestDivisor(a,b):
    if(len(a)%len(b)!=0):
        return(-1)
    m=len(a)
    n=len(b)
    r=0
    c=""
    while(r<=(m-n)):
        c+=b
        r+=n
        if(c==a):
            return(len(set(b)))
        
# print(findSmallestDivisor("bcdbcdbcdbcd","bcdbcd"))
 
# Driver Code
if __name__ == '__main__':
    S, T = "bcdbcdbcdbcd", "bcdbcd"
    print(findSmallestDivisor(S, T))