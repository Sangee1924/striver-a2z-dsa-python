def RomanToInteger(num):
    Roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    ans=0
    for i in range(len(num)):
        if (i < len(num)-1) and (Roman[num[i]] < Roman[num[i+1]]):
            ans-=Roman[num[i]]
        else:
            ans+=Roman[num[i]]
    return ans

num = input("Enter Roman NUmber: ")
print(RomanToInteger(num))