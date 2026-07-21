def Max_k_Odd(s,k):
    left=0
    count=0
    ans=0
    for right in range(len(s)):
        if s[right]%2==1:
            count+=1
        while count > k:
            if s[left]%2==1:
                count-=1
            left+=1
        ans+= (right-left+1)
    return ans
def NiceSubstring(s,k):
    return Max_k_Odd(s,k) - Max_k_Odd(s,k-1)

s = list(map(int,input("Enter user Input : ").split()))
k = int(input("Enter distinct char in substring: "))
print(NiceSubstring(s,k))