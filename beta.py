# lets create two classes:

class Node:
    def __innit__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __innit__(self):
        self.head = None

    def insert_at_begining(self, data):

        node = Node(data, self.head)
        self.head=node
        

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)


ll = LinkedList()
ll.insert_at_begining(45)
ll.insert_at_begining(43)
ll.print()