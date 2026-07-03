# Find the repeating and missing numbers

def Repeating_missingM2(arr):
    xor=0
    for i in arr:
        xor^=i
    for i in range(1,n+1):
        xor^=i
    bit = xor & -xor
    one=0
    zero=0
    for i in arr:
        if i & bit:
            one^=i
        else:
            zero^=i
    for j in range(1,n+1):
        if j & bit:
            one^=j
        else:
            zero^=j
    if arr.count(one)==2:
        print([one,zero])
    else:
        print([zero,one])

n = int(input("Enter Length of Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
Repeating_missingM2(arr)