# Kadane's Algo

def maxSubArray(arr):
    sum=0
    maxi=float('-inf')
    for i in range(n):
        if sum==0: start=i
        sum+=arr[i]
        if sum>maxi:
            maxi=sum
            ans_start=start 
            ans_End = i
        if sum<0:
            sum=0
    print("Max subarray element :",arr[ans_start:ans_End+1])
    print("Max subArray value:",maxi)

n= int(input("Length of Arr: "))
arr = []
for i in range(n):
    val = int(input("Enter val  : "))
    arr.append(val)
maxSubArray(arr)















n= int(input("Length of Arr: "))
arr = []
for i in range(n):
    val = int(input("Enter val  : "))
    arr.append(val)
maxSubArray(arr)