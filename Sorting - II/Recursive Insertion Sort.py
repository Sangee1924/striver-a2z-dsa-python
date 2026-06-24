def Recursive_Insertion(arr,i):
    j=i
    if (i>=n):
        return
    while(j>0 and arr[j-1]>arr[j]):
        temp = arr[j-1]
        arr[j-1] = arr[j]
        arr[j]= temp
        j-=1
    Recursive_Insertion(arr,i+1)


n = int(input("Enter the Length:"))
arr=[]
for i in range(n):
    val = int(input("Enter val: "))
    arr.append(val)

Recursive_Insertion(arr,0)
print(arr)