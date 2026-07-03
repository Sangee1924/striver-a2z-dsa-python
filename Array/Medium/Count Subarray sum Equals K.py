def BruteForce_subarrayEqualsK(arr,k):
    count=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if sum==k:
                count+=1
    print("BruteForce_subarrayEqualsK : ",count)

def optimal_subarrayEqualsK(arr,k):
    perfixSum = {0:1}
    sum=0
    count=0
    for i in range(n):
        sum+=arr[i]
        rem = sum - k
        if rem in perfixSum:
            count+=perfixSum[rem]
        perfixSum[sum] = perfixSum.get(sum,0)+1
    print("optimal_subarrayEqualsK : ",count)


n= int(input("Length of Arr: "))
arr = []
for i in range(n):
    val = int(input("Enter val  : "))
    arr.append(val)
k = int(input("Enter the K : "))
BruteForce_subarrayEqualsK(arr,k)
optimal_subarrayEqualsK(arr,k)