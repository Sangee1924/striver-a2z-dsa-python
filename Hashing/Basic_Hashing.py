def hashing_Num_count(arr):
    hash=[0]*13
    for i in range(n):
        hash[arr[i]] = hash[arr[i]] + 1
    q = int(input("Enter Total Num to check Count: "))
    for j in range(q):
        num = int(input("Number : "))
        print(hash[num])




n = int(input("Enter length of Arr :"))
arr = []
for i in range(n):
    val = int(input("Enter Arr Val : "))
    arr.append(val)
hashing_Num_count(arr)