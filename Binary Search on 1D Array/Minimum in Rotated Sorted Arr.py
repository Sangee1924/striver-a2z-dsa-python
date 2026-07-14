def minimun(arr):
    low=0
    high=n-1
    mini=float('inf')
    while(low<=high):
        mid=(low+high)//2
        if arr[low] < arr[high]:
            mini=min(mini,arr[low])
            break
        if arr[mid] > arr[low]:
            mini=min(mini,arr[low])
            low=mid+1
        else:
            mini=min(mini,arr[mid])
            high=mid-1
    print("Minimum in Rotated Sorted Array :",mini)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
minimun(arr)