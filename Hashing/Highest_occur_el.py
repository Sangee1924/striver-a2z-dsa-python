def Highest_occurrence(arr):
    hash=[0]*13
    for i in range(n):
        hash[arr[i]] += 1
    max_count = max(hash)
    max_val= hash.index(max_count)
    print("Highest Qccurrence Number",max_val)

n = int(input("Enter length of Arr :"))
arr = []
for i in range(n):
    val = int(input("enter val:"))
    arr.append(val)

Highest_occurrence(arr)