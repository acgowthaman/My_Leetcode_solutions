class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = ListNode(0)
        p2 = p1
        while list1 and list2:
            if list1.val <= list2.val:
                p2.next = list1
                list1 = list1.next
            else:
                p2.next = list2
                list2 = list2.next
            p2 = p2.next
        p2.next = list1 or list2
        return p1.next
