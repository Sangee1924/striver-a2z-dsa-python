def sortByFreq(s):
    freq={}
    for i in s:
        freq[i]=freq.get(i,0)+1
    reqfreq = sorted(freq.items(), key=lambda x: (-x[1],x[0]))
    ans=[]
    for key,val in reqfreq:
        ans.append(key)
    return ans