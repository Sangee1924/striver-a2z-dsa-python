def MajorityEl1(nums):
    hash = {}
    for i in range(len(nums)):
        hash[nums[i]] = hash.get(nums[i],0)+1
    maxi=0
    maxElement=0
    for key,value in hash.items():
        if value>maxi:
            maxi=value
            maxElement=key
    print(maxElement)

n= int(input("Length of Arr: "))
arr = []
for i in range(n):
    val = int(input("Enter val  : "))
    arr.append(val)
MajorityEl1(arr)