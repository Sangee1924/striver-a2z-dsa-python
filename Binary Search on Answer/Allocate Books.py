def AllocationPossible(arr,mid):
    student=1
    pages=0
    for i in arr:
        if pages+i <= mid:
            pages+=i
        else:
            student+=1
            pages=i  
    return student

def AllocateBooks(arr,k):
    low=min(arr)
    high=sum(arr)
    while(low<=high):
        mid=(low+high)//2
        if AllocationPossible(arr,mid) <= k:
            high=mid-1
        else:
            low=mid+1
    return low

n = int(input("Enter the length of Array: "))
arr=[]
for i in range(n):
    val= int(input("Enter Array value :"))
    arr.append(val)
k= int(input("Enter no of Student : "))
print(AllocateBooks(arr,k))