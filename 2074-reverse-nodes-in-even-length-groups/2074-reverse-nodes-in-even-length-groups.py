# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode(0,head)
        p=d
        g=1
        while p.next:
            c=p.next
            t=c
            k=0
            while t and k<g:
                t=t.next
                k+=1
            if k%2==0:
                prev=t
                cur=c
                for _ in range(k):
                    nxt=cur.next
                    cur.next=prev
                    prev=cur
                    cur=nxt
                p.next=prev
                p=c
            else:
                for _ in range(k):
                    p=p.next
            g+=1
        return d.next
        