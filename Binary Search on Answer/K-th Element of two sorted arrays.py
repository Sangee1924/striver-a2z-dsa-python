def KthElement(arr,arr2,k):
    if len(arr2) < len(arr):
        return KthElement(arr2,arr,k)
    n1=len(arr)
    n2=len(arr2)
    low=max(0,k-n2)
    high=min(k,n1)
    while(low<=high):
        cut1= (low+high)//2
        cut2= k - cut1

        L1 = float('-inf') if cut1==0 else arr[cut1-1]
        L2 = float('-inf') if cut2==0 else arr2[cut2-1]
        R1 = float('inf') if cut1==n1 else arr[cut1]
        R2 = float('inf') if cut2==n2 else arr2[cut2]

        if L1<=R2 and L2<=R1:
            return max(L1,L2)
        elif L1>R2:
            high=cut1-1
        else:
            low=cut1+1
    return 0

n = int(input("Enter the length of Array: "))
arr=[]
for i in range(n):
    val= int(input("Enter Array value :"))
    arr.append(val)
n2 = int(input("Enter the length of Array: "))
arr2=[]
for i in range(n2):
    val= int(input("Enter Array value :"))
    arr2.append(val)
k = int(input("Enter Kth Element : "))
print(KthElement(arr,arr2,k))