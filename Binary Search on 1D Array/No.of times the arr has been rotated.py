def RotationTimes(arr):
    low=0
    high=n-1
    mini=float('inf')
    index=-1
    while(low<=high):
        mid=(low+high)//2
        if arr[low]<arr[high]:
            if arr[low]<mini:
                mini=arr[low]
                index=low
            break
        if arr[low]<=arr[mid]:
            if arr[low]<mini:
                mini=arr[low]
                index=low
            low=mid+1
        else:
            if arr[mid]<mini:
                mini=arr[mid]
                index=mid
            high=mid-1
    print(index)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
RotationTimes(arr)