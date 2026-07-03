# Find the repeating and missing numbers

def Repeating_missing(arr):
    arr.sort()
    Repeating=-1
    Missing=-1
    if arr[0]!=1:
        Missing=1
    for i in range(1,n):
        if (arr[i]==arr[i-1]):
            Repeating = arr[i]
        if (arr[i]-arr[i-1]==2):
            Missing=arr[i]-1
    if arr[-1]!=n:
        Missing=n
    print([Repeating,Missing])

n = int(input("Enter Length of Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
Repeating_missing(arr)