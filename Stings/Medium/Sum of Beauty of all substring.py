def SumOfBeauty(s):
    n=len(s)
    total=0
    for i in range(n):
        freq={}
        for j in range(i,n):
            freq[s[j]]=freq.get(s[j],0)+1

            value = freq.values()
            maxi = max(value)
            mini = min(value)

            total+=(maxi-mini)
    return total

s = input("Enter String : ")
print(SumOfBeauty(s))