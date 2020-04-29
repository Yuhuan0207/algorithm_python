class LinkedList:
    """
    Implementation of singly Linked List. 
    """
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None
        if nodes:
            node = Node(value = nodes.pop(0))
            self.head = node
            self.tail = self.head
            for elem in nodes:
                node.next = Node(value = elem)                
                node = node.next
                if node:
                    self.tail = node

    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return "->".join(str(n) for n in nodes)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Node:
    """
    Implementation of Singly Linked List Node.
    """
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value


class LinkedListOperation:
    def getNthNodeValue(self, n, head):
        """
        Return Nth node in the given LinkedList
        """        
        if n == 1:
            return head
                
        while n > 1 and head:
            head = head.next
            n -= 1
        return head.value
    
    def appendNode(self, llist, node):
        if not node:
            return
        llist.tail.next = node
        llist.tail = node
        return

    def sortLinkedListNode(self, llist):
        if not llist:
            return llist

        zero_list, one_list, two_list = LinkedList([-1]), LinkedList([-1]), LinkedList([-1])
        node_iter = iter(llist)
        for node in node_iter:
            if node.value == 0:
                self.appendNode(zero_list, node)
            elif node.value == 1:
                self.appendNode(one_list, node)
            else:
                self.appendNode(two_list, node)

        zero_list.tail.next = one_list.head.next
        one_list.tail.next = two_list.head.next
        return zero_list.head.next

    def deleteNodes(self, llist, target_node):
        if not target_node:
            return llist
        
        dummy_node = Node(value = -1)
        dummy_node.next = llist.head
        cur_node = dummy_node
        while cur_node:
            if cur_node.next and cur_node.next.value == target_node.value:
                self.deleteNodeHelper(llist.head, llist.tail, cur_node.next, cur_node)
                # next_node = cur_node.next.next
                # cur_node.next = next_node
            cur_node = cur_node.next
        return dummy_node.next

    def deleteNodeHelper(self, head, tail, to_delete, prev_node):
        if not to_delete:
            return
        if to_delete == head:
            head = to_delete.next
        if to_delete == tail:
            tail = prev_node
        if prev_node:
            prev_node.next = to_delete.next

    def reverseLinkedList(self, llist):
        prev_node = None        
        if not llist.head:
            return llist.head
        return self.reverseLinkedListHelper(prev_node, llist.head, llist.head.next)

    def reverseLinkedListHelper(self, prev_node, cur_node, next_node):
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        return prev_node

if __name__ == "__main__":
    test = [
        [1,2,0,1,0,1,0,2]
    ]
    for arr in test:        
        llist = LinkedList(arr[:])
        llist3 = LinkedList(arr[:])
        print(llist)
        print(llist3)
        print("head: " + str(llist.head.value))
        print("tail: " + str(llist.tail.value))
        print(LinkedListOperation().getNthNodeValue(2, llist.head))
        print("-----")
        new_llist = LinkedList(arr)
        print("Sort Nodes in Linked List: " + str(new_llist))
        a = LinkedListOperation().sortLinkedListNode(new_llist)
        while a:
            print(a.value)
            a = a.next
        print("-----")
        new_llist2 = LinkedList(arr)
        print("Delete node 1 in Linked List: " + str(llist))
        b = LinkedListOperation().deleteNodes(llist, Node(1))
        while b:
            print(b.value)
            b = b.next

        print("-----")
        print("Linked list before reverse: " + str(llist3))
        c = LinkedListOperation().reverseLinkedList(llist3)
        while c:
            print(c.value)
            c = c.next