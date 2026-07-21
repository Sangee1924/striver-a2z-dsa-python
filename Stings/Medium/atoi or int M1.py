def atoi(s):
    sign=1
    i=0
    ans=0
    while (i<len(s) and s[i]==" "):
        i+=1
    if i<len(s) and s[i]=="-":
        sign=-1
        i+=1
    elif i<len(s) and s[i]=="+":
        sign=1
        i+=1
    while(i<len(s) and '0' <= s[i] <= '9'):
        ans = ans*10 + int(s[i])
        i+=1
    ans*= sign

    if ans > (2**31)-1:
        return (2**31)-1
    elif ans < -(2**31):
        return -(2**31)
    
    return ans

s = input("Enter User Input : ")
print(atoi(s))