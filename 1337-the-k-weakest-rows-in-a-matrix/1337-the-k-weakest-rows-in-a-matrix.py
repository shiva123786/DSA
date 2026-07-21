class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr=[]
        for i,row in enumerate(mat):
            arr.append((sum(row),i))
        arr.sort()
        return [i for _,i in arr[:k]]