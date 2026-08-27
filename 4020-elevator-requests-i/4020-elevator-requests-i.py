class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        ans=0
        cur=0
        for x in requests:
            ans+=abs(cur-x)
            cur=x
        return ans