class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def find_min(self):
        if not self.left:
            return self.data
        if self.left:
            return self.left.find_min()

    def find_max(self):
        if not self.right:
            return self.data
        if self.right:
            return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return left_sum + right_sum + self.data

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()
        elements.append(self.data)
        return elements

    def search(self, data):
        if self.data == data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False


def build_tree(elements):
    root = BinaryTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    root = build_tree(numbers)
    print(root)
    print(root.in_order_traversal())
    print(root.pre_order_traversal())
    print(root.post_order_traversal())
    print(root.search(29))
    print(root.find_min())
    print(root.find_max())
    print(root.calculate_sum())
