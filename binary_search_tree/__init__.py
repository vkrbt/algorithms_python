class TreeNode:
    def __init__(self, value):
        self.left = None;
        self.right = None;
        self.data = value;

class Tree:
    def __init__(self):
        self.root = None;

    def addNode(self, node, value):
        if(node==None):
            self.root = TreeNode(value);
        else:
            if(value<node.data):
                if(node.left==None):
                    node.left = TreeNode(value)
                else:
                    self.addNode(node.left, value);
            else:
                if(node.right==None):
                    node.right = TreeNode(value)
                else:
                    self.addNode(node.right, value);

    def printInorder(self, node):
        if(node!=None):
            self.printInorder(node.left)
            print(node.data)
            self.printInorder(node.right)

def main():
    testTree = Tree()
    testTree.addNode(testTree.root, 200)
    testTree.addNode(testTree.root, 300)
    testTree.addNode(testTree.root, 100)
    testTree.addNode(testTree.root, 30)
    testTree.printInorder(testTree.root)