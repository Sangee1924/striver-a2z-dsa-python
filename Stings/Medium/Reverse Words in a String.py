def ReverseWords(string):
    temp=""
    i=len(string)-1
    end=i+1
    while(i>=0):
        while(i>=0 and string[i]==" "):
            i-=1
        if i<0:
            break

        end=i

        while(i>=0 and string[i]!=" "):
            i-=1
        word=string[i+1:end+1]

        if temp!="":
            temp+=" "
        temp+=word
    return temp
