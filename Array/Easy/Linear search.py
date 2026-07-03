def LinearSearch(arr,num):
    for i in range(n):
        if arr[i]==num:
            print(i)
            break
    else:
        print(-1)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
num= int(input("Enter number to find index: "))
LinearSearch(arr,num)