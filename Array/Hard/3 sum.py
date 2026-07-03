# 3 Sum : Find triplets that add up to a zero
def ThreeSum(arr):
    arr.sort()
    ans=[]
    for i in range(n-2):
        j=i+1
        k=n-1
        if(i>0 and arr[i]==arr[i-1]): continue
        while(j<k):
            sums = arr[i]+arr[j]+arr[k]
            if sums==0:
                ans.append([arr[i],arr[j],arr[k]])
                j+=1
                k-=1
                while(j<k and arr[j]==arr[j-1]): j+=1
                while(j<k and arr[k]==arr[k+1]): k-=1
            elif sums<0:
                j+=1
            else:
                k-=1
    print(ans)

n = int(input("Enter Length of a Array : "))
arr =[]
for i in range(n):
    val = int(input("Enter the value : "))
    arr.append(val)
ThreeSum(arr)