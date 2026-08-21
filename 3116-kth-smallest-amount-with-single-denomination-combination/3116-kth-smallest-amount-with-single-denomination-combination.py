class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n=len(coins)

        def check(x):
            cnt=0
            for mask in range(1,1<<n):
                lcm=1
                bits=0
                for i in range(n):
                    if mask>>i&1:
                        lcm=lcm*coins[i]//gcd(lcm,coins[i])
                        if lcm>x:
                            break
                        bits+=1
                if bits%2:
                    cnt+=x//lcm
                else:
                    cnt-=x//lcm
            return cnt>=k

        l,r=1,k*min(coins)
        while l<r:
            mid=(l+r)//2
            if check(mid):
                r=mid
            else:
                l=mid+1
        return l