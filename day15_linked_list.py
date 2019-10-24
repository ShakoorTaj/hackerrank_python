class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
        temp = Node(data)
        if head is None:
            head = temp
            return head
        current = head
        while current.next is not None:
            current = current.next
        current.next = temp
        return head

mylist= Solution()
T=1
head=None
for i in range(T):
    data=[1,2,3,4]
    head=mylist.insert(head,data)
mylist.display(head)