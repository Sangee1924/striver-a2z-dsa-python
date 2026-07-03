# 4 Sum | Find Quads that add up to a target value

def FourSum(arr,target):
    ans=[]
    arr.sort()
    for i in range(n-3):
        if (i>0 and arr[i]==arr[i-1]): continue
        for j in range(i+1,n-2):
            if(j>i+1 and arr[j]==arr[j-1]): continue
            k=j+1
            l=n-1
            while(k<l):
                sums=arr[i]+arr[j]+arr[k]+arr[l]
                if sums==target:
                    ans.append([arr[i],arr[j],arr[k],arr[l]])
                    k+=1
                    l-=1
                    while(k<l and arr[k]==arr[k-1]):k+=1
                    while(k<l and arr[l]==arr[l+1]): l-=1
                elif sums<target:
                    k+=1
                else:
                    l-=1
    print(ans)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
target = int(input("Enter target : "))
FourSum(arr,target)