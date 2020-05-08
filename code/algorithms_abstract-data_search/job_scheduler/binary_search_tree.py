class Node:

    def __init__(self, key):
        self.data = key
        self.left_child = None
        self.right_child = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key.data > current.data:
            if current.right_child == None:
                current.right_child = key
            else:
                self._insert(current.right_child, key)
        elif key.data < current.data:
            if current.left_child == None:
                current.left_child = key
            else:
                self._insert(current.left_child, key)

    def find_val(self, key):
        return self._find_val(self.root, key)

    def _find_val(self, current, key):
        if current:
            if key == current.data:
                return "Value found in tree"
            elif key < current.data:
                return self._find_val(current.left_child, key)
            else:
                return self._find_val(current.right_child, key)
        return 'Value not found in tree'

    def min_right_subtree(self, curr):
        if curr.left_child == None:
            return curr
        else:
            return self.min_right_subtree(curr.left_child)

    def delete_val(self, key):
        self._delete_val(self.root, None, None, key)

    def _delete_val(self, current, prev, is_left, key):
        if current:
            if key == current.data:
                if current.left_child and current.right_child:
                    min_child = self.min_right_subtree(current.right_child)
                    current.data = min_child.data
                    self._delete_val(current.right_child, current, False, min_child.data)
                elif current.left_child == None and current.right_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = None
                        else:
                            prev.right_child = None
                    else:
                        self.root = None
                elif current.left_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = current.right_child
                        else:
                            prev.right_child = current.right_child
                    else:
                        self.root = current.right_child
                else:
                    if prev:
                        if is_left:
                            prev.left_child = current.left_child
                        else:
                            prev.right_child = current.left_child
                    else:
                        self.root = current.left_child
            elif key < current.data:
                self._delete_val(current.left_child, current, True, key)
            elif key > current.data:
                self._delete_val(current.right_child, current, False, key)
        else:
            print(f"{key} not found in Tree")

    def in_order(self):
        # left, root, right
        self._in_order(self.root)
        print("")

    def _in_order(self,current):
        if current:
            self._in_order(current.left_child)
            print(current.data, end=" ")
            self._in_order(current.right_child)

    def post_order(self):
        # right, root, left
        self._post_order(self.root)
        print("")

    def _post_order(self, current):
        if current:
            self._post_order(current.right_child)
            print(current.data, end=" ")
            self._post_order(current.left_child)
