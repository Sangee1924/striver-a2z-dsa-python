def Max_K_Distinct(s,k):
    left=0
    freq={}
    ans=0
    for right in range(len(s)):
        freq[s[right]]=freq.get(s[right],0)+1

        while len(freq)>k:
            freq[s[left]]-=1
            if freq[s[left]]==0:
                del freq[s[left]]
            left+=1
        
        ans+=(right-left+1)
    return ans

def Count_substring(s,k):
    return (Max_K_Distinct(s,k) - Max_K_Distinct(s,k-1))


s = input("Enter user Input : ")
k = int(input("Enter distinct char in substring: "))
print(Count_substring(s,k))