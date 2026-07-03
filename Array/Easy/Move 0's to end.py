def Move_0_end(arr):
    j=0
    for i in range(n):
        if arr[i]==0:
            j=i
            break
    for k in range(n):
        if arr[k]!=0:
            temp=arr[k]
            arr[k]=arr[j]
            arr[j]=temp
            j+=1
    print(arr)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
Move_0_end(arr)