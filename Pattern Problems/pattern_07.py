n = int(input())

for i in range(1,n+1):
    space= 2*(n-i)
    star = (i*2)-1
    print(" "*space + "* "*star)
