def sums(arr,mid):
    total=0
    for i in arr:
        total += (i+mid-1)//mid
    return total

def SmallestDivisor(arr,limit):
    ans=0
    low=1
    high=max(arr)
    while(low<=high):
        mid=(low+high)//2
        if sums(arr,mid) <=limit:
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
limit= int(input("Enter Threshold (limit) : "))
print(SmallestDivisor(arr,limit))