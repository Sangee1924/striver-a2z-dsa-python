def FindSqrt(num):
    ans=1
    low=1
    high=num
    while(low<=high):
        mid=(low+high)//2
        if (mid*mid)<=num:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans              # You can return ans or high

num = int(input("Enter an number:"))
print("Sqrt of a number using Binary Search :",FindSqrt(num))