def Floor_Ceil(arr,low,high,target):
    floor=0        
    ceil=0
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]<=target:
            floor=arr[mid]
            low=mid+1
        else:
            high=mid-1
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>=target:
            ceil=arr[mid]
            high=mid-1
        else:
            low=mid+1
    print(floor)
    print(ceil)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
target = int(input("Enter target: "))
Floor_Ceil(arr,0,n-1,target)