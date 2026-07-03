# Maximum Product Subarray in an Array

def MaxProductSubarray(arr):
    prifix_prod=1
    sufix_prod=1
    maxi=float('-inf')
    for i in range(n):
        prifix_prod*=arr[i]
        sufix_prod*=arr[len(arr)-i-1]
        if prifix_prod == 0:
            prifix_prod=1
        if sufix_prod == 0:
            sufix_prod=1
        maxi = max(maxi,prifix_prod,sufix_prod)
    print(maxi)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
MaxProductSubarray(arr)