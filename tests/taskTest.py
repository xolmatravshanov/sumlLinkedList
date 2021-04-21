import unittest
from main import LinkedList
from add import addTwoLinkedList


class TestTask(unittest.TestCase):

    def test_first_case(self):
        list1 = LinkedList()
        list1.push(2)
        list1.push(4)
        list1.push(3)
        list2 = LinkedList()
        list2.push(5)
        list2.push(6)
        list2.push(4)

        newList = addTwoLinkedList(list1.head, list2.head)
        newList.reverse()
        newList.printList()
        self.assertEqual(newList.head.data, 7)

    def test_second_case(self):
        # input  l1 = [9,9,9,9,9,9,9]
        list3 = LinkedList()
        i = 0
        while i < 7:
            list3.push(9)
            i += 1
        # input   l2 = [9,9,9,9]
        list4 = LinkedList()
        j = 0
        while j < 4:
            list4.push(9)
            j += 1

        newList = addTwoLinkedList(list3.head, list4.head)
        newList.reverse()
        newList.printList()
        self.assertEqual(newList.head.data, 8)