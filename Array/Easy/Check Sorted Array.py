def CheckSorted(arr):
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
    return True

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)

print("True" if CheckSorted(arr) else "False")
