class Node:
    def __init__(self, data, color="RED"):
        self.data = data
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0, "BLACK")
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, data):
        node = Node(data)
        node.parent = None
        node.left = self.NIL
        node.right = self.NIL
        node.color = "RED"

        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = "BLACK"
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == "RED":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "BLACK"

    def inorder_helper(self, node):
        if node != self.NIL:
            self.inorder_helper(node.left)
            print(f"{node.data}({node.color})", end=" ")
            self.inorder_helper(node.right)

    def inorder(self):
        self.inorder_helper(self.root)

    def search_tree_helper(self, node, key):
        if node == self.NIL or key == node.data:
            return node
        if key < node.data:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    def search_tree(self, k):
        return self.search_tree_helper(self.root, k)

if __name__ == "__main__":
    rbt = RedBlackTree()
    
    print("插入节点: 7, 3, 18, 10, 22, 8, 11, 26")
    nodes = [7, 3, 18, 10, 22, 8, 11, 26]
    
    for node in nodes:
        rbt.insert(node)
    
    print("中序遍历红黑树:")
    rbt.inorder()
    print()
    
    print("搜索节点 10:")
    result = rbt.search_tree(10)
    if result != rbt.NIL:
        print(f"找到节点: {result.data}({result.color})")
    else:
        print("未找到节点")
        
    print("搜索节点 15:")
    result = rbt.search_tree(15)
    if result != rbt.NIL:
        print(f"找到节点: {result.data}({result.color})")
    else:
        print("未找到节点")