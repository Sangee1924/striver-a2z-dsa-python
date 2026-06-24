def recursive_Bubble(arr,i):
    if (i>=n):
        return
    didSwap = 0
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            didSwap=1
    
    if didSwap==0:
        return
    
    recursive_Bubble(arr,i+1)


n = int(input("Enter the Length:"))
arr=[]
for i in range(n):
    val = int(input("Enter val: "))
    arr.append(val)

recursive_Bubble(arr,0)
print(arr)