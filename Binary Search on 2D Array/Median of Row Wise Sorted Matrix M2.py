def smaller(matrix,mid,n,m):
    cnt=0
    for i in range(n):
        low=0
        high=m-1
        ans=m
        while(low<=high):
            mid1=(low+high)//2
            if matrix[i][mid1]>mid:
                ans=mid1
                high=mid1-1
            else:
                low=mid1+1
        cnt+=ans
    return cnt

def Median(matrix):
    n=len(matrix)
    m=len(matrix[0])
    low=min(row[0] for row in matrix)
    high=max(row[m-1] for row in matrix)
    req= (m*n)//2
    while(low<=high):
        mid=(low+high)//2
        cnt = smaller(matrix,mid,n,m)
        if cnt <= req:
            low=mid+1
        else:
            high=mid-1
    return low

n = int(input("Enter no of Rows = "))
m = int(input("Enter no of Columns = "))
matrix=[]
for i in range(n):
    row=[]
    for j in range(m):
        val = int(input("Enter the Value :"))
        row.append(val)
    matrix.append(row)
print(Median(matrix))