def Insertion_sort(arr,n):
    for i in range(n):
        j=i
        while (j>0 and arr[j-1] > arr[j]):
            temp = arr[j]
            arr[j]=arr[j-1]
            arr[j-1] = temp
            j-=1
    print("Sorted Array :",arr)




n = int(input("Enter Length: "))
arr = []
for i in range(n):
    val = int(input("enter Val :"))
    arr.append(val)

Insertion_sort(arr,n)