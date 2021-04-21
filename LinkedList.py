from Node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, nodeData):
        new_node = Node(nodeData)
        new_node.next = self.head
        self.head = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            print(temp)
