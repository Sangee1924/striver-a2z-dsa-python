def BSUB(arr,low,high,target):
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    print(ans)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
target = int(input("Enter target: "))
BSUB(arr,0,n-1,target)