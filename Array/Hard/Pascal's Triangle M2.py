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
    return ans

def pascalM2(R):
    row=[]
    for i in range(1,R+1):
        row.append(pascalM1(R,i))
    print(f"Pascal Triangle {R}th Row:",row)

R = int(input("Enter the Row Value: "))
pascalM2(R)
