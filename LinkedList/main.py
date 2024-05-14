class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data, None)
        if not self.head:
            self.head = node
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node

    def remove_at(self, idx):
        if idx < 0:
            raise Exception

        if idx == 0:
            self.head = self.head.next

        itr = self.head
        counter = 0
        while itr.next:
            if counter == (idx - 1):
                itr.next = itr.next.next
                break
            counter += 1
            itr = itr.next

    def insert_at(self, idx, data):
        if idx < 0:
            raise Exception

        if idx == 0:
            self.head = self.head.next

        itr = self.head
        counter = 0
        while itr.next:
            if counter == (idx - 1):
                itr.next = Node(data, itr.next)
                break
            counter += 1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        if not self.head:
            return

        itr = self.head

        while itr.next:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        if not self.head:
            return

        itr = self.head

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
            itr = itr.next

    # Remove first node that contains data

    def print(self):
        itr_head = self.head
        if self.head:
            while itr_head:
                print(itr_head.data)
                itr_head = itr_head.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining(55)
    ll.insert_at_begining(65)
    ll.insert_at_end(88)
    ll.insert_at(1, 99)
    ll.insert_after_value(55, 101)
    ll.remove_by_value(99)
    # ll.remove_at(1)

    ll.print()
