# Brute Force approach

def Gas_Station(arr,k):
    N = len(arr)
    HowMany=[0]*(N-1)
    for i in range(k):
        maxSection=-1
        maxInd=-1
        for j in range(N-1):
            distance = arr[j+1] - arr[j]
            sectionLen = distance/(HowMany[j]+1)
            if sectionLen > maxSection:
                maxSection= sectionLen
                maxInd=j
        HowMany[maxInd]+=1
    maxAns=0
    for i in range(N-1):
        distance= arr[i+1] - arr[i]
        sectionLen = distance / (HowMany[i]+1)
        maxAns = max(maxAns,sectionLen)
    
    return maxAns

n = int(input("Enter the length of Array: "))
arr=[]
for i in range(n):
    val= int(input("Enter Array value :"))
    arr.append(val)
k= int(input("Enter no of Gas Station : "))
print("Minimise Maximum Distance between Gas Stations :",Gas_Station(arr,k))