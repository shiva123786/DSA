class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        res=[0]*(len(num1)+len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                a=ord(num1[i])-ord('0')
                b=ord(num2[j])-ord('0')
                product=a*b
                p1=i+j
                p2=i+j+1
                total=product+res[p2]
                res[p2]=total%10
                res[p1]+=total//10
        ans=""
        for x in res:
            if ans or x!=0:
                ans+=str(x)
        return ans