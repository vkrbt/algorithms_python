class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.root = value if isinstance(value, Node) else None

    def add(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
        else:
            current = self.root
            while True:
                if value == current.value:
                    break
                if value < current.value:
                    if not current.left:
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if not current.right:
                        current.right = node
                        break
                    else:
                        current = current.right
        return node.value

    def __contains__(self, item):
        found = False
        current = self.root
        while not found and current:
            if item == current.value:
                found = True
                break
