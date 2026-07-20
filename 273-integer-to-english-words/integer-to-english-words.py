class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        below20=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        def helper(n):
            if n==0:
                return ""
            if n<20:
                return below20[n]+" "
            if n<100:
                return tens[n//10]+" "+helper(n%10)
            return below20[n//100]+" Hundred "+helper(n%100)
        ans=""
        if num>=1000000000:
            ans+=helper(num//1000000000)+"Billion "
            num%=1000000000
        if num>=1000000:
            ans+=helper(num//1000000)+"Million "
            num%=1000000
        if num>=1000:
            ans+=helper(num//1000)+"Thousand "
            num%=1000
        ans+=helper(num)
        return ans.strip()