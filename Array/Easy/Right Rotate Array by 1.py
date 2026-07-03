def RightRotate(arr):
    temp=[0]
    for i in range(n):
        if i==n-1:
            temp[0]=arr[i]
        else:
            temp.append(arr[i])
    print(temp)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
RightRotate(arr)