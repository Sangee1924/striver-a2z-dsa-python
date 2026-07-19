def Search(matrix,target):
    n=len(matrix)
    m=len(matrix[0])
    for i in range(n):
        low=0
        high=m-1
        while(low<=high):
            mid=(low+high)//2
            if matrix[i][mid]==target:
                return True
            elif matrix[i][mid]>target:
                high=mid-1
            else:
                low=mid+1
    return False

n = int(input("Enter no of Rows = "))
m = int(input("Enter no of Columns = "))
matrix=[]
for i in range(n):
    row=[]
    for j in range(m):
        val = int(input("Enter the Value :"))
        row.append(val)
    matrix.append(row)
target = int(input("Enter the num to find : "))
print(Search(matrix,target))