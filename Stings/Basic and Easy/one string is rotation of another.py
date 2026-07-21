def Rotation(s,goal):
    if len(s) != len(goal):
        return False
    double = s+s
    return (goal in double)

s=input("Enter String one : ")
goal=input("Enter String Two : ")
print(Rotation(s,goal))