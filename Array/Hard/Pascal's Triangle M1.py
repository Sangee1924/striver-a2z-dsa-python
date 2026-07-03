def fact(n):
    if n<=0:
        return 1
    return n * fact(n-1)

def pascalM1(r,c):
    r-=1
    c-=1
    nu = fact(r)
    d1 = fact(c)
    d2  =fact(r-c)
    ans = nu//(d1*d2)
    print(f"Pascal triangle {r} row and {c} col:",ans)

R = int(input("Enter Row Value: "))
C = int(input("Enter Col Value: "))
pascalM1(R,C)
