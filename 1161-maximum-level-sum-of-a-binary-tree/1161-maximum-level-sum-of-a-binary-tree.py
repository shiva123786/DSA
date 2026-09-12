# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        ans=1
        mx=float("-inf")
        level=1
        while q:
            s=0
            for _ in range(len(q)):
                node=q.popleft()
                s+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if s>mx:
                mx=s
                ans=level
            level+=1
        return ans