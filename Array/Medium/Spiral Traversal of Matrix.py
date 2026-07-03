def spiral(matrix):
    ans=[]
    left=0
    right=m-1
    top=0
    bottom=n-1
    while (top<=bottom and left<=right):
        for i in range(left,right+1):
            ans.append(matrix[top][i])
        top+=1
        for i in range(top,bottom+1):
            ans.append(matrix[i][right])
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                ans.append(matrix[bottom][i])
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                ans.append(matrix[i][left])
            left+=1
    print(ans)

n = int(input("Enter No.of Rows : "))
m = int(input("Enter No.of Col : "))
matrix=[]
for i in range(n):
    row=[]
    for j in range(m):
        val = int(input("Enter val : "))
        row.append(val)
    matrix.append(row)
spiral(matrix)