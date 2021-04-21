from main import Node
from main import LinkedList


# 2ta linked list bo'sa ular har bir element qo'shish kerak
# agar 10 ga teng yoki 10 yuqori bo'lsa uni qoldiqi olish kerak va
# yodlab qolish kerak butun qismini
# har birini srazi yangi linked listga qo'shib
# oxirda o'sha linked listni qaytarish kerak


def addTwoLinkedList(list1: Node, list2: Node):
    if list1 is None or list2 is None:
        return ValueError('two list must given for function')

    sum = 0

    returnLinkedList = LinkedList()

    while list1 is not None or list2 is not None:

        adder = sum

        if list1 is not None:
            adder += list1.data
            list1 = list1.next

        if list2 is not None:
            adder += list2.data
            list2 = list2.next

        if returnLinkedList.head is None:
            returnLinkedList.head = Node(adder % 10)
        else:
            returnLinkedList.push(adder % 10)

        sum = adder // 10

    if sum > 0:
        returnLinkedList.push(sum)

    return returnLinkedList
