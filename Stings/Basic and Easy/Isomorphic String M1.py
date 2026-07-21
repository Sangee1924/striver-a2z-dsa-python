def Isomorphic(s,t):
    mapST={}
    mapTS={}
    for i in range(len(s)):
        if s[i] not in mapST:
            mapST[s[i]]=t[i]
        elif mapST[s[i]]!=t[i]:
            return False
        
        if t[i] not in mapTS:
            mapTS[t[i]]=s[i]
        elif mapTS[t[i]]!=s[i]:
            return False
    return True

s=input("Enter String one : ")
t=input("Enter String Two : ")
print(Isomorphic(s,t))