# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        while not (list1 == None and list2 == None):
            if list1 == None and list2 != None:
                return list2
            elif list1 != None and list2 == None:
                return list1
            elif list1.val <= list2.val:
                return ListNode(list1.val, Solution.mergeTwoLists(list1.next, list2))
            else:
                return ListNode(list2.val, Solution.mergeTwoLists(list1, list2.next))