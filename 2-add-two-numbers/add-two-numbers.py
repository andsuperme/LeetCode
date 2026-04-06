# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1 = []
        num2 = []

        while l1:
            num1.append(str(l1.val))
            l1 = l1.next
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next
        
        # reverse and convert to int
        num1 = int("".join(num1[::-1]))
        num2 = int("".join(num2[::-1]))

        res = num1 + num2

        dummy = ListNode()
        ans = dummy
        
        # build result linked list
        dummy = ListNode()
        cur = dummy

        for digit in str(res)[::-1]:
            cur.next = ListNode(int(digit))
            cur = cur.next

        return dummy.next