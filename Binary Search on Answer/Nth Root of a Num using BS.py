def Root(N,mid):
    ans=1
    for i in range(N):
        ans*=mid
    return ans

def NthRoot(N,M):
    ans=-1
    low=1
    high=M
    while(low<=high):
        mid=(low+high)//2
        if Root(N,mid) == M:
            ans=mid
            break
        elif Root(N,mid) > M:
            high=mid-1
        else:
            low=mid+1
    return ans

N = int(input("Enter an Number: "))
M = int(input("Enter an Number: "))
print(NthRoot(N,M))