class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class TreeIterator:
    def __init__(self, root):
        self.stack = [root]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration()
        node = self.stack.pop()
        for child in node.children:
            self.stack.append(child)
        return node.value

my_tree = Node(1)
my_tree.children.append(Node(2))
my_tree.children.append(Node(3))
my_tree.children[0].children.append(Node(4))

my_iterator = TreeIterator(my_tree)
for value in my_iterator:
    print(value)