from typing import Optional 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class List:
    def __init__(self, node_list: list): 
        if len(node_list) == 0:
            self.head = None
            return None
        self.list = ListNode(node_list[0])
        self.head = self.list
        for i in range(1, len(node_list)):
            self.list.next = ListNode(node_list[i])
            self.list = self.list.next
    def get_list(self):
        return self.head

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        if list1 or list2:
            tail.next = list1 if list1 else list2
        return head.next


list1 = List([]).get_list()
list2 = List([1, 3, 4]).get_list()
sol = Solution().mergeTwoLists(list1, list2)
while sol:
    print(sol.val)
    sol = sol.next
