class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a=sorted([(v,i)for i,v in enumerate(score)],reverse=True)
        sol=[""]*len(score)
        for i,(_,idx) in enumerate(a):
            if i==0:
                sol[idx]="Gold Medal"
            elif i==1:
                sol[idx]="Silver Medal"
            elif i==2:
                sol[idx]="Bronze Medal"
            else:
                sol[idx]=str(i+1)
        return sol