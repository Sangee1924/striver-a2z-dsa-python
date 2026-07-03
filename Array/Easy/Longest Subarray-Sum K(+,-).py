def longestSub(arr,k):
    PerMap={}
    sum=0
    maxLen=0
    for i in range(n):
        sum += arr[i]
        if sum==k:
            maxLen = max(maxLen,i+1)
        rem = sum-k
        if rem in PerMap:    
            lens = i - PerMap[rem]
            maxLen = max(maxLen,lens)
        if sum not in PerMap:
            PerMap[sum]=i

    print("Longest subarray Length:",maxLen)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
k = int(input("enter:"))
longestSub(arr,k)