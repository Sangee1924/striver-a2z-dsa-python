def majorityEl(nums):
    hash={}
    res=[]
    for i in range(len(nums)):
        hash[nums[i]]= hash.get(nums[i],0)+1
    for key,value in hash.items():
        if value > (len(nums)/3):
            res.append(key)
    print(res)


n= int(input("Length of Arr: "))
arr = []
for i in range(n):
    val = int(input("Enter val  : "))
    arr.append(val)
majorityEl(arr)