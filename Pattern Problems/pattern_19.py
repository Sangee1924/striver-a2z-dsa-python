n = int(input())

for i in range(n):
    print("* "*(n-i) + "  "*(i*2) + "* "*(n-i))

for j in range(1,n+1):
    print("* "*(j) + "  "*(2*(n-j)) + "* "*j)