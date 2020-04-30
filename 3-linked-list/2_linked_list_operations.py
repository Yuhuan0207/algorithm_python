import math
class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val

class LinkedListOperations:
    def createLinkedList(self, arr):
        """
        Create Linked List with values in input array.
        :type: 
        """
        return

    def mergeTwoLists(self, l1, l2):
        """
        Leetcode 21. Merge Two Sorted Lists
        """
        dummy_head = ListNode(1)
        cur_node = dummy_head
        while l1 and l2:
            if l1.val <= l2.val:
                cur_node.next = l1
                l1 = l1.next
            else:
                cur_node.next = l2
                l2 = l2.next
            cur_node = cur_node.next
        if l1:
            cur_node.next = l1
        if l2:
            cur_node.next = l2
        return dummy_head.next

    def insertionSortList(self, head):
        """
        Leetcode 147. Insertion Sort List
        """
        prev_node = dummy_node = ListNode(math.inf)
        dummy_node.next = head
        cur_node = head
        while cur_node and cur_node.next:
            #find the node that needs to be sorted
            sorting_val = cur_node.next.val
            if cur_node.val <= sorting_val:
                cur_node = cur_node.next
                continue
            
            #once find cur_node, find prev_node
            if prev_node.val > sorting_val:
                prev_node = dummy_node
            while prev_node.next.val <= sorting_val:
                prev_node = prev_node.next
            
            tmp_node = cur_node.next
            cur_node.next = tmp_node.next
            tmp_node.next = prev_node.next
            prev_node.next = tmp_node
        return dummy_node.next

    def deleteNode(self, node):
        """
        Leetcode 237. Delete Node in a Linked List
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node:
            return 
        
        node.val = node.next.val
        while node.next.next:
            node = node.next 
            node.val = node.next.val
        node.next = None
        return

    def reverseList(self, head):
        """
        Leetcode 206. Reverse Linked List
        """
        if not head:
            return head
                
        prev_node = head
        cur_node = head.next
        head.next = None
        return self.reverseListHelper(prev_node, cur_node)
                
    def reverseListHelper(self, prev_node, cur_node):
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        return prev_node



if __name__ == "__main__":
    # validated on Leetcode
    pass
    