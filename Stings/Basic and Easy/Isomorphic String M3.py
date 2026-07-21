def Isomorphic(s,t):
    return (len(set(zip(s,t))) == len(set(s)) == len(set(t)))

s=input("Enter String one : ")
t=input("Enter String Two : ")
print(Isomorphic(s,t))