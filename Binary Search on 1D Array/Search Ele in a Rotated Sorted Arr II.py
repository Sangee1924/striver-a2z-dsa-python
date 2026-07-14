def SearchII(arr,target):
    low = 0
    high = n
    while (low<high):
        mid = (low+high)//2
        if arr[mid]==target:
            return True
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low+=1
            high-=1
            continue
        if arr[low]<arr[mid]:
            if target >= arr[low] and target < arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if target > arr[mid] and target <= arr[high]:
                low=mid+1
            else:
                high=mid-1
    return False

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
target = int(input("Enter target: "))
print(SearchII(arr,target))