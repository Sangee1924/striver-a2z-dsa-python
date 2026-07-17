def missingNum(arr,k):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        missing = arr[mid] - (mid+1)
        if missing < k:
            low=mid+1
        else:
            high=mid-1
    return low+k




n = int(input("Enter the length of Array: "))
arr=[]
for i in range(n):
    val= int(input("Enter Array value :"))
    arr.append(val)
k= int(input("Enter positive Int : "))
print(missingNum(arr,k))