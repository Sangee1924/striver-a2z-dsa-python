def NoOfInnerParentheses(s):
    cnt=0
    freq=0    
    for i in s:
        if i=="(":
            if cnt>0:
                freq+=1
            cnt+=1
        elif i==")":
            if cnt>1:
                freq+=1
            cnt-=1
    return freq//2

s = input("Enter User input : ")
print(NoOfInnerParentheses(s))