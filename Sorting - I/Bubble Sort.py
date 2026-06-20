def Bubble_sort(arr,n):
    for i in range(n-1):
        DidSwap = 0
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]= temp
                DidSwap = 1
        if DidSwap == 0:
            break
    print(arr)



n= int(input("Length of Arr: "))
arr = []
for i in range(n):
    val = int(input("Enter val  : "))
    arr.append(val)
Bubble_sort(arr,n)