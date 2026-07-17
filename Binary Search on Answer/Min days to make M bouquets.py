def check(arr,mid,k):
    cnt=0
    bouquets=0
    for i in arr:
        if i<=mid:
            cnt+=1
        else:
            bouquets += (cnt//k)
            cnt=0
    bouquets += (cnt//k)
    return bouquets


def miniDays(arr,m,k):
    if n < m*k:
        return -1
    ans=0
    low=min(arr)
    high=max(arr)
    while(low<=high):
        mid=(low+high)//2
        if check(arr,mid,k) >=m:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
m = int(input("Enter No Of bouquets: "))
k = int(input("Enter no of roses in Bouquets: "))
print(miniDays(arr,m,k))