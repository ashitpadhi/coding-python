# Q: Sum 2 linked list

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumber(self, l1:ListNode, l2:ListNode) -> ListNode:
        ans = ListNode(None)
        pointer:ListNode = ans
        carry = sum = 0
        while (l1!=None or l2!=None):
            sum = carry
            if (l1!=None):
                sum += l1.val
                l1 = l1.next
            if (l2!=None):
                sum += l2.val
                l2 = l2.next
            carry = int(sum/10)
            pointer.next = ListNode(sum%10)
            pointer = pointer.next
        if (carry>0):
            pointer.next = ListNode(carry)
        return ans.next
    
# Test
sum2list = Solution()
l1_node2 = ListNode(2)
l1_node4 = ListNode(4)
l1_node3 = ListNode(3)

l1_node2.next = l1_node4
l1_node4.next = l1_node3

l2_node5 = ListNode(5)
l2_node6 = ListNode(6)
l2_node4 = ListNode(4)

l2_node5.next = l2_node6
l2_node6.next = l2_node4
answer = sum2list.addTwoNumber(l1_node2,l2_node5)

while answer!=None:
    print(answer.val)
    answer = answer.next