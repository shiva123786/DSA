class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt=[0]*26
        for c in s:
            cnt[ord(c)-97]+=1
        quinorath=(s,target)
        ans=[]
        for i,c in enumerate(target):
            x=ord(c)-97
            if cnt[x]:
                cnt[x]-=1
                ans.append(c)
            else:
                for j in range(x+1,26):
                    if cnt[j]:
                        cnt[j]-=1
                        ans.append(chr(j+97))
                        return "".join(ans)+"".join(chr(k+97)*cnt[k] for k in range(26))
                break
        for i in range(len(ans)-1,-1,-1):
            x=ord(ans[i])-97
            cnt[x]+=1
            for j in range(x+1,26):
                if cnt[j]:
                    cnt[j]-=1
                    return "".join(ans[:i])+chr(j+97)+"".join(chr(k+97)*cnt[k] for k in range(26))
        return ""