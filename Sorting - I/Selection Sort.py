def selection_sort(n,arr):
    for i in range(n-1):
        mini=i
        for j in range(i,n):
            if arr[j] < arr[mini]:
                mini=j
        temp = arr[i]
        arr[i] = arr[mini]
        arr[mini] = temp
    print("Sorted Array :",arr)


n = int(input("Length of Arr: "))
arr=[]
for i in range(n):
    val = int(input("Enter val : "))
    arr.append(val)
    
selection_sort(n,arr)