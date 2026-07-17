import heapq

def Gas_Station(arr,k):
    N = len(arr)
    howMany=[0]*(N-1)
    heapMax=[]
    for i in range(N-1):
        heapq.heappush(heapMax,(-(arr[i+1]-arr[i]),i))
    for j in range(k):
        sectionMax , MaxInd= heapq.heappop(heapMax)
        sectionMax = - sectionMax
        howMany[MaxInd]+=1
        NewSectionLen = (arr[MaxInd+1] - arr[MaxInd])/(howMany[MaxInd]+1)
        heapq.heappush(heapMax,(-NewSectionLen,MaxInd))

    maxAns,index= heapq.heappop(heapMax)
    return -maxAns

n = int(input("Enter the length of Array: "))
arr=[]
for i in range(n):
    val= int(input("Enter Array value :"))
    arr.append(val)
k= int(input("Enter no of Gas Station : "))
print("Minimise Maximum Distance between Gas Stations :",Gas_Station(arr,k))