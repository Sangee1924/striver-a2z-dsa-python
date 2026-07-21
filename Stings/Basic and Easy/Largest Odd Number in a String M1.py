def LargestOdd(s):
    i=len(s)
    while(i>0):
        if int(s[i-1])%2!=0:
            ans=s[:i].lstrip("0")
            return ans if ans else ""
        i-=1
    return ""

s=input("Enter a string: ")
print(LargestOdd(s))