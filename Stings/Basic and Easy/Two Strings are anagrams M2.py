def Anagrams(s,t):
    if len(s) != len(t):
        return False
    
    count=[0]*26
    for i in s:
        count[ord(i)-ord('A')]+=1

    for j in t:
        count[ord(j)-ord('A')]-=1

    for i in count:
        if i!=0:
            return False
        
    return True

s=input("Enter String one : ")
t=input("Enter String Two : ")
print(Anagrams(s,t))