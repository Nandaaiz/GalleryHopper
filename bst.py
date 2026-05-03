from node import Node

class BST:
    def __init__(self):
        self.root = None

    #Inserts a new gallery into the tree ps:exhibition_date removed for now
    def insert(self, name, neighborhood, art_style, type, alias=None):
        new_node = Node(name, neighborhood, art_style, type, alias)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    #Compares names to find the correct position for the new node
    def _insert_recursive(self, current, new_node):
        if new_node.name < current.name:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    #Searches for a gallery by name (case-insensitive)
    def search(self, name):
        return self._search_recursive(self.root, name.lower())

    #Recursively compares names to find the gallery
    def _search_recursive(self, current, name):
        if current is None:
            return  None
        if name == current.name.lower():
            return current
        # check alias
        if current.alias:
            if any(name == a.lower() for i in current.alias):
                return current
        elif name < current.name.lower():
            return self._search_recursive(current.left, name)
        else:
            return self._search_recursive(current.right,name)

    #Returns all the galleries in alphabetical order
    def list_all(self):
        galleries = []
        self._in_order(self.root, galleries)
        return galleries

    #Traverses the tree in order: left, root, right
    def _in_order(self, current, galleries):
        if current is None:
            return
        self._in_order(current.left, galleries)
        galleries.append(current)
        self._in_order(current.right, galleries)