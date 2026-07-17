def total(arr,mid):
    days=1
    load=0
    for i in arr:
        if load+i <= mid:
            load+=i
        else:
            days+=1
            load=i
    return days
def Capacity(arr,d):
    ans=0
    low=max(arr)
    high=sum(arr)
    while(low<=high):
        mid=(low+high)//2
        if total(arr,mid) <= d:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

n = int(input("Enter the length of Array: "))
arr=[]
for i in range(n):
    val= int(input("Enter Array value :"))
    arr.append(val)
d= int(input("Enter Days : "))
print(Capacity(arr,d))