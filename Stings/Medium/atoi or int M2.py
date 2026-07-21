def helper(i,sign,ans,s,n):
    if i>=n or not s[i].isdigit():
        return sign*ans
    ans=ans*10 + int(s[i])
    num=sign*ans
    if num > (2**31)-1:
        return (2**31)-1
    elif num < -(2**31):
        return -(2**31)
    return helper(i+1,sign,ans,s,n)

def atoi(s):
    n=len(s)
    sign=1
    ans=0
    i=0
    while(i<n and s[i]==" "):
        i+=1
    if (i<n and (s[i]=="-" or s[i]=="+")):
        if s[i]=="-":
            sign=-1
        i+=1
    return helper(i,sign,ans,s,n)



s = input("Enter User Input : ")
print(atoi(s))