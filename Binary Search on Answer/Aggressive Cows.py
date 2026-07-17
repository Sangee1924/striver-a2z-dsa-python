def check(arr,mid):
    cow=1
    last=arr[0]
    for i in range(1,n):
        if arr[i] - last >= mid:
            cow+=1
            last=arr[i]
        else:
            continue
    return cow

def AggressiveCow(arr,k):
    low=1
    high=max(arr)-min(arr)
    while(low<=high):
        mid=(low+high)//2
        if check(arr,mid)>=k:
            low=mid+1
        else:
            high=mid-1
    return high

n = int(input("Enter the length of Array: "))
arr=[]
for i in range(n):
    val= int(input("Enter Array value :"))
    arr.append(val)
k= int(input("Enter no of Aggressive Cows : "))
arr.sort()
print(AggressiveCow(arr,k))