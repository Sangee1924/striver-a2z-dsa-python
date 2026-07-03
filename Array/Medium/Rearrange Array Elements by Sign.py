def RearrangeBySign(arr):
    positive=0
    negative=1
    ans=[0]*n
    for i in range(n):
        if arr[i]>0:
            ans[positive]=arr[i]
            positive+=2
        elif arr[i]<0:
            ans[negative]=arr[i]
            negative+=2
    print(ans)


n= int(input("Length of Arr: "))
arr = []
for i in range(n):
    val = int(input("Enter val  : "))
    arr.append(val)
RearrangeBySign(arr)