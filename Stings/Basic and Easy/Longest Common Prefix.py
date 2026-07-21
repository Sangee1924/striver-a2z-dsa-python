def longestCommon(s):
    if not s:
        return ""
    n=min(len(word) for word in s)
    for i in range(n):
        for j in range(len(s)-1):
            if s[j][i]!=s[j+1][i]:
                return s[0][:i] 
    return s[0][:n] 