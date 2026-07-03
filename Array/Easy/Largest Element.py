# Brute Force
print("Brute Force")
def sort(arr,i):
    j=i
    if i>=n:
        return
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
    sort(arr,i+1)
n = int(input("Enter length:"))
arr=[]
for i in range(n):
    val = int(input("Enter the Value : "))
    arr.append(val)
sort(arr,0)
print("Largest Element in array is",arr[n-1])
print("-"*40)


# Optimal Approach
print("Optimal Approach")
def Largest_Element(arr):
    largest = arr[0]
    for i in range(n):
        if arr[i]>largest:
            largest=arr[i]
    return largest
n = int(input("Enter Length of a Array : "))
arr_1 =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr_1.append(val)
print(Largest_Element(arr_1))