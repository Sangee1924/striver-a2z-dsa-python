def check(arr,mid):
    total=0
    subarray=1
    for i in arr:
        if total+i <= mid:
            total+=i
        else:
            subarray+=1
            total=i
    return subarray

def splitArray(arr,k):
    low=max(arr)
    high=sum(arr)
    while(low<=high):
        mid=(low+high)//2
        if check(arr,mid) <= k:
            high=mid-1
        else:
            low=mid+1
    return low

n = int(input("Enter the length of Array: "))
arr=[]
for i in range(n):
    val= int(input("Enter Array value :"))
    arr.append(val)
k= int(input("Enter no of subarrays : "))
print(splitArray(arr,k))