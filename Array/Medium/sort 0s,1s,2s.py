def sort012(arr):
    for i in range(n-1):
        mini=i
        for j in range(i,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[mini],arr[i]=arr[i],arr[mini]
    print(arr)

n= int(input("Length of Arr: "))
arr = []
for i in range(n):
    val = int(input("Enter val  : "))
    arr.append(val)
sort012(arr)