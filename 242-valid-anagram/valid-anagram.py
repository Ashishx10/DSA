class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h={}
        n=len(s)
        m=len(t)
        if n!=m:
            return False
        for i in range(n):
            if s[i] in h:
                h[s[i]]+=1
            else:
                h[s[i]]=1
        for j in range(m):
            if t[j] not in h:
                return False
            h[t[j]]-=1
            if h[t[j]]<0:
                return False
        return True
