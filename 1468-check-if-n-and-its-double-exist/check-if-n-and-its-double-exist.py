class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        n=len(arr)
        for i,x in enumerate(arr):
            j=bisect_left(arr,x*2)
            if j<n and arr[j]==x*2 and j!=i:
                return True
        return False
        