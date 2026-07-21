def expand(l,r,s):
    while(l>=0 and r<len(s) and s[l]==s[r]):
        l-=1
        r+=1
    return s[l+1:r]

def LongestPalindrome(s):
    res=""
    for i in range(len(s)):
        Max_Palindrome1= expand(i,i,s)
        if len(Max_Palindrome1) > len(res):
            res=Max_Palindrome1
        Max_Palindrome2 = expand(i,i+1,s)
        if len(Max_Palindrome2)>len(res):
            res=Max_Palindrome2
    return res

s = input("Enter String : ")
print(LongestPalindrome(s))