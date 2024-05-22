import time
from collections import deque
import threading


class FoodOrder:
    def __init__(self):
        self.order_queue = deque()

    def place_order(self, items):
        for item in items:
            self.order_queue.appendleft(item)
            time.sleep(1)

    def serve_order(self):
        while self.order_queue:
            order = self.order_queue.pop()
            print(f"Serving order {order}")
            time.sleep(1.5)


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]


def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()


if __name__ == "__main__":
    # orders = ["pizza", "samosa", "pasta", "biryani", "burger"]
    # order_system = FoodOrder()
    # t1 = threading.Thread(target=order_system.place_order, args=(orders,))
    # t2 = threading.Thread(target=order_system.serve_order)
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    produce_binary_numbers(10)
