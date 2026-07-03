#Count the number of subarrays with given xor K

def SubArrayXor_K(arr,k):
    mpp={}
    xor=0
    count=0
    for i in range(n):
        xor^=arr[i]
        if xor == k:
            count+=1
        rem = xor^k
        if rem in mpp:
            count+=mpp[rem]
        mpp[xor]=mpp.get(xor,0)+1
    print(count)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
k = int(input("Enter K value: "))
SubArrayXor_K(arr,k)