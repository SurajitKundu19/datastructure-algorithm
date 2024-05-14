class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if not self.head:
            return

        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

    def print_backward(self):
        if not self.head:
            return

        itr = self.get_last_node()
        while itr.prev:
            print(itr.data)
            itr = itr.prev

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def insert_at_begining(self, data):
        node = Node(data, self.head, None)
        if self.head:
            self.head.prev = node
        self.head = node


if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.insert_at_begining(11)
    ll.insert_at_begining(22)
    ll.insert_at_begining(33)
    ll.print_forward()
