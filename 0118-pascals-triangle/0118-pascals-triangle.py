class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri=[]
        for i in range(numRows):
            row=[1]*(1+i)
            for j in range(1,i):
                row[j]=tri[i-1][j-1]+tri[i-1][j]
            tri.append(row)
        return tri
        