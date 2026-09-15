class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans=[]
        for i in range(1,len(searchWord)+1):
            p=searchWord[:i]
            l=0
            r=len(products)
            while l<r:
                m=(l+r)//2
                if products[m]<p:
                    l=m+1
                else:
                    r=m
            ans.append([x for x in products[l:l+3] if x.startswith(p)])
        return ans