def stockProfit(arr):
    mini=arr[0]
    MaxProfit=0
    for i in range(n):
        SellingP = arr[i]-mini
        MaxProfit = max(MaxProfit, SellingP)
        mini = min(mini,arr[i])
    print(MaxProfit)



n= int(input("Length of Arr: "))
arr = []
for i in range(n):
    val = int(input("Enter val  : "))
    arr.append(val)
stockProfit(arr)