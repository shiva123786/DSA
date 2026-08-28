class Solution:
    def lexPalindromicPermutation(self,s,target):
        n=len(s)
        count=[0]*26

        for c in s:
            count[ord(c)-97]+=1

        odd=0
        mid=-1

        for i in range(26):
            if count[i]%2:
                odd+=1
                mid=i

        if n%2==0 and odd!=0:
            return ""
        if n%2==1 and odd!=1:
            return ""

        half=n//2
        left=[x//2 for x in count]

        copy=left[:]
        matched=0
        fullMatch=True

        for i in range(half):
            c=ord(target[i])-97
            if copy[c]==0:
                fullMatch=False
                break
            copy[c]-=1
            matched+=1

        def build(firstHalf):
            rev=firstHalf[::-1]
            if n%2:
                return firstHalf+chr(mid+97)+rev
            return firstHalf+rev

        if fullMatch:
            firstHalf=target[:half]
            answer=build(firstHalf)
            if answer>target:
                return answer

        use=left[:]

        for i in range(matched):
            use[ord(target[i])-97]-=1

        for pos in range(min(matched,half-1),-1,-1):
            if pos<matched:
                use[ord(target[pos])-97]+=1

            tChar=ord(target[pos])-97

            for c in range(tChar+1,26):
                if use[c]>0:
                    use[c]-=1

                    firstHalf=target[:pos]+chr(c+97)
                    rest=[]

                    for x in range(26):
                        rest.extend([chr(x+97)]*use[x])

                    return build(firstHalf+"".join(rest))

        return ""