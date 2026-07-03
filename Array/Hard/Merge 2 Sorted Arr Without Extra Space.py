# Merge two Sorted Arrays Without Extra Space

def mergeSortedArray(arr1,arr2,n,m):
    i=n-1
    j=m-1
    k=n+m-1
    while(i>=0 and j>=0):
        if arr1[i]>arr2[j]:
            arr1[k]=arr1[i]
            k-=1
            i-=1
        elif arr1[i]<arr2[j]:
            arr1[k]=arr2[j]
            k-=1
            j-=1
        else:
            arr1[k]=arr1[i]
            k-=1
            j-=1
    while (j>=0):
        arr1[k]=arr2[j]
        k-=1
        j-=1
    print("----------Answer----------")
    print("Merged Arrays Without Extra Space:",arr1)

n = int(input("Enter Length of a Array 1 : "))
arr1 =[]
for i in range(n):
    val = int(input("Enter the value of arr1 : "))
    arr1.append(val)
n1=int(input("Enter non zero element in arr1: "))
m = int(input("Enter Length of a Array 2 : "))
arr2 =[]
for i in range(m):
    val = int(input("Enter the value of arr2 : "))
    arr2.append(val)
mergeSortedArray(arr1,arr2,n1,m)