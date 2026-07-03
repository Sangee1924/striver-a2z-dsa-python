def leaders(arr):
    maxi=float('-inf')
    Leader=[]
    for i in range(n-1,-1,-1):
        if arr[i]>maxi:
            Leader.append(arr[i])
        maxi = max(maxi,arr[i])
    Leader.reverse()
    print(Leader)

n= int(input("Length of Arr: "))
arr = []
for i in range(n):
    val = int(input("Enter val  : "))
    arr.append(val)
leaders(arr)