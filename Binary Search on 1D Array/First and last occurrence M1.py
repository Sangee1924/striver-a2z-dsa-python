def Occurrence(arr,target):
    def firstocc(arr,target):
        low=0
        high=n-1
        first=-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]==target:
                first=mid
                high=mid-1
            elif arr[mid]> target:
                high=mid-1
            else:
                low=mid+1
        print("First Occurrence :",first)
    def lastocc(arr,target):
        low=0
        high=n-1
        Last=-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]==target:
                Last=mid
                low=mid+1
            elif arr[mid]> target:
                high=mid-1
            else:
                low=mid+1
        print("Last Occurrence  :",Last)
    firstocc(arr,target)
    lastocc(arr,target)


n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
target = int(input("Enter target: "))
Occurrence(arr,target)