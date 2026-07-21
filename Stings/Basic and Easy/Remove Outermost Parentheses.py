def RemoveParentheses(string):
    temp=""
    cnt=0
    for i in string:
        if i=="(":
            cnt+=1
            if cnt>1:
                temp+="("
        elif i==")":
            cnt-=1
            if cnt>0:
                temp+=")"
    return temp

string=input("enter: ")
print(RemoveParentheses(string))