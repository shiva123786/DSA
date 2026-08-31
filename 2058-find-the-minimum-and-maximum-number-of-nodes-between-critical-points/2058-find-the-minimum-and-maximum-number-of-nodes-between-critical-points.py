# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        curr=head.next
        pos=1
        first=-1
        last=-1
        mn=float("inf")

        while curr and curr.next:
            if (curr.val>prev.val and curr.val>curr.next.val) or (curr.val<prev.val and curr.val<curr.next.val):
                if first!=-1:
                    mn=min(mn,pos-last)
                else:
                    first=pos
                last=pos
            prev=curr
            curr=curr.next
            pos+=1

        if first==-1 or first==last:
            return [-1,-1]

        return [mn,last-first]