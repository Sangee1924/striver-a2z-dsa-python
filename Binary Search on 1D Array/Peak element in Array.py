def Peak(arr):
    n=len(arr)
    if n==1:
        return 0
    if arr[0]>arr[1]:
        return 0
    if arr[n-1]>arr[n-2]:
        return n-1
    low=1
    high=n-2
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]>arr[mid-1]:
            low=mid+1
        else:
            high=mid-1
    return -1

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
print(Peak(arr))