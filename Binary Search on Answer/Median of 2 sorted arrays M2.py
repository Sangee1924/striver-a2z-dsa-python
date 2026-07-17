def median(arr,arr2):
    if len(arr2)<len(arr):
        return median(arr2,arr)
    n1=len(arr)
    n2=len(arr2)
    low=0
    high=n1
    while(low<=high):
        cut1=(low+high)//2
        cut2=((n1+n2+1)//2) - cut1

        L1 = float('-inf') if cut1==0 else arr[cut1-1]
        L2 = float('-inf') if cut2==0 else arr2[cut2-1]
        R1 = float('inf') if cut1==n1 else arr[cut1]
        R2 = float('inf') if cut2==n2 else arr[cut2]

        if L1 <= R2 and L2 <= R1:
            if (n1 + n2) % 2 == 0:
                return (max(L1, L2) + min(R1, R2)) / 2.0
            else:
                return max(L1, L2)
        elif L1>R2:
            high=cut1-1
        else:
            low=cut1+1
    return 0.0

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
print(median(arr,arr2))