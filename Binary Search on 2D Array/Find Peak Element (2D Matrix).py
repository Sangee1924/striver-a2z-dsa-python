def MaxRow(matrix,mid,n):
    ind=-1
    maxEle=-1
    for i in range(n):
        if matrix[i][mid]>maxEle:
            maxEle=matrix[i][mid]
            ind=i
    return ind

def PeakEle(matrix):
    n=len(matrix)
    m=len(matrix[0])
    low=0
    high=m-1
    while(low<=high):
        mid=(low+high)//2
        Row  = MaxRow(matrix,mid,n)
        left = -1 if mid-1<0 else matrix[Row][mid-1]
        right= -1 if mid+1>m-1 else matrix[Row][mid+1]

        if matrix[Row][mid] > left and matrix[Row][mid] > right:
            return [Row,mid]
        elif matrix[Row][mid]<left:
            high=mid-1
        else:
            low=mid+1
    return [-1,-1]

n = int(input("Enter no of Rows = "))
m = int(input("Enter no of Columns = "))
matrix=[]
for i in range(n):
    row=[]
    for j in range(m):
        val = int(input("Enter the Value :"))
        row.append(val)
    matrix.append(row)
print(PeakEle(matrix))