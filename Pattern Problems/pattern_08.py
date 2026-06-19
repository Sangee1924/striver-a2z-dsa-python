n = int(input())

for i in range(n,0,-1):
    space = 2*(n-i)
    star = (i*2)-1
    print(" "*space + "* "*star)
