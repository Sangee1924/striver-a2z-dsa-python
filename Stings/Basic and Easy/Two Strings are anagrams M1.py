def Anagrams(s,t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

s=input("Enter String one : ")
t=input("Enter String Two : ")
print(Anagrams(s,t))