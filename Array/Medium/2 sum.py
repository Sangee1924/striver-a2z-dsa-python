def TwoSum(arr,k):
    mp={}
    for i in range(n):
        rem = k - arr[i]
        if rem in mp:
            print(True)
            break
        mp[arr[i]] = i
    else:
        print(False)

n= int(input("Length of Arr: "))
arr = []
for i in range(n):
    val = int(input("Enter val  : "))
    arr.append(val)
k = int(input("Enter element: "))
TwoSum(arr,k)