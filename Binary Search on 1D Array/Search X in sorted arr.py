def BS1(arr,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return BS1(arr,mid+1,high,target)
    return BS1(arr,low,mid-1,target)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
target = int(input("Enter target: "))
ans = BS1(arr,0,n-1,target)
print(ans)