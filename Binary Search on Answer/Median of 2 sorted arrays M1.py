def median(arr,arr2):
    left=0
    right=0
    ans=[]
    while (left<len(arr) and right<len(arr2)):
        if arr[left]<=arr2[right]:
            ans.append(arr[left])
            left+=1
        else:
            ans.append(arr2[right])
            right+=1        
    while (left<len(arr)):
        ans.append(arr[left])
        left+=1

    while (right<len(arr2)):
        ans.append(arr2[right])
        right+=1
    N= len(ans)
    if N%2==0:
        median= (ans[N//2] + ans[(N//2)-1])/2.0
    else:
        median = ans[N//2]

    return median

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