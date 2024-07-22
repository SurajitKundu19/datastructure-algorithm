class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None


    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def print_tree(self, print_level):
        level = self.get_level()
        if level <= print_level:
            prefix = level * " "
            print(prefix, self.name, self.designation)
            for child in self.children:
                child.print_tree(print_level)


def add_element_to_tree():
    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(TreeNode("Chinmoy", "CTO"))
    ceo.add_child(TreeNode("Gels", "HR Head"))
    return ceo


if __name__ == "__main__":
    root = add_element_to_tree()
    root.print_tree(1)
