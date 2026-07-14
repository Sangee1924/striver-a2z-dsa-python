def BSLB(arr,target):
    low=0
    high=n-1
    first=n
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>=target:
            first=mid
            high=mid-1
        else:
            low=mid+1
    return first
def BSUB(arr,target):
    low=0
    high=n-1
    last=n
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>target:
            last=mid
            high=mid-1
        else:
            low=mid+1
    return last-1

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
target = int(input("Enter target: "))
lb = BSLB(arr,target)
if (lb==n or arr[lb] != target):
    print(-1,-1)
else:
    print(lb,BSUB(arr,target))