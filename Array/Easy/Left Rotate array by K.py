def LeftRotateBy_K(arr,k):
    temp=arr[:k]
    for i in range(n-k):
        arr[i]= arr[k+i]
    for j in range(k):
        arr[k+j+1]=temp[j]
    print(arr)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
k = int(input("Enter Rotation Time : "))
LeftRotateBy_K(arr,k)