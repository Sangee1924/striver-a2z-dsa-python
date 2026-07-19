def Search(matrix,target):
    n=len(matrix)
    m=len(matrix[0])
    low=0
    high=(n*m)-1
    while(low<=high):
        mid=(low+high)//2
        ind1=mid//m
        ind2=mid%m
        if matrix[ind1][ind2]==target:
            return True
        elif matrix[ind1][ind2]<target:
            low=mid+1
        else:
            high=mid-1
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