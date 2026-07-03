# Length of the longest subarray with zero Sum

def LongSubarr(arr):
    mpp={}
    sums=0
    maxi=0
    for i in range(n):
        sums+=arr[i]
        if sums == 0:
            maxi = max(maxi,i+1)
        if sums in mpp:
            maxi = max(maxi,i-mpp[sums])
        else:
            mpp[sums]=i
    print(maxi)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
LongSubarr(arr)