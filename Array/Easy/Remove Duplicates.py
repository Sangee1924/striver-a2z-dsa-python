# Brute Force
def Bruteforce_RemoveDuplicate(arr):
    sets=set()
    for i in range(n):
        sets.add(arr[i])
    result=list(sets)
    print(result)

def Optimal_removeDupicate(arr):
    i=0
    for j in range(1,n):
        if (arr[i] != arr[j]):
            arr[i+1] = arr[j]
            i=i+1
    print(arr[:i+1])


n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
Bruteforce_RemoveDuplicate(arr)
Optimal_removeDupicate(arr)