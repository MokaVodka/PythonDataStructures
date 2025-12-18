class AvlNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.height = 1

    def _update_height(self):
        leftHeight = 0 if self.left is None else self.left.height
        rightHeight = 0 if self.right is None else self.right.height
        self.height = 1 + max(leftHeight, rightHeight)

    def add(self, val):
        # Add value to left or right
        if val < self.value:
            if self.left is None:
                self.left = AvlNode(val, None, None)
            else:
                self.left.add(val)
        elif val > self.value:
            if self.right is None:
                self.right = AvlNode(val, None, None)
            else:
                self.right.add(val)

        # Update height
            self._update_height()

    def __str__(self):
        txt = ""
        if self.left is not None:
            txt += self.left.__str__()
        txt += str(self.value) + " "
        if self.right is not None:
            txt += self.right.__str__()
        return txt

    def count(self):
        count = 1

        if self.left is not None:
            count += self.left.count()
        if self.right is not None:
            count += self.right.count()

        return count

    def max_depth(self):
        count, leftCount, rightCount = 1, 0, 0

        if self.left is not None:
            leftCount += self.left.max_depth()
        if self.right is not None:
            rightCount += self.right.max_depth()

        return count + max(leftCount, rightCount)

    def dot(self, parent):
        txt = ''

        if parent is not None:
            txt += f'  {parent.value} -- {self.value}\n'

        if self.left is not None:
            txt += self.left.dot(self)

        if self.right is not None:
            txt += self.right.dot(self)

        return txt

    # -- This is for delete()
    def _get_largest(self, parent, maxNode=None):
        maxNode = self if maxNode is None else maxNode

        if maxNode.value < self.value:
            maxNode = self

        if self.right is not None:
            parent, maxNode = self.right._get_largest(self, maxNode)

        return parent, maxNode

    def _replace_child(self, node, replacement):
        if self.left is node:
            self.left = replacement
        elif self.right is node:
            self.right = replacement

    # Find node X to be deleted
    # - Case 1: X with no left child ==> replace X with right child of X
    # - Case 2: X as a left child ==> find max in left subtree,
    #           move max value to X and remove max node
    def delete(self, value, parent):
        deleteNode = False

        # Same as search
        if value < self.value:
            if self.left is not None:
                deleteNode = self.left.delete(value, self)

        elif value > self.value:
            if self.right is not None:
                deleteNode = self.right.delete(value, self)

        # Start deletion
        elif value == self.value:
            deleteNode = True

            # Case 1: no left child
            # Replace self on parent to self.right
            if self.left is None:
                parent._replace_child(self, self.right)

            # Case 2: has left child
            else:
                # Get max value of left branch
                maxParent, maxNode = self.left._get_largest(self)

                # Override max value to current node
                self.value = maxNode.value

                # Replace largest with largest.left on largest parent
                if maxNode.left is not None:
                    maxParent._replace_child(maxNode, maxNode.left)

                # Delete largest on largest parent
                else:
                    maxParent._replace_child(maxNode, None)

        return deleteNode


#
# The class AvlSet
#
class AvlSet:

    def __init__(self):
        self.root = None

    # Adds value val to tree (if it doesn't already exist)
    def add(self, val):
        if self.root is None:
            self.root = AvlNode(val, None, None)
        else:
            self.root.add(val)

    # Returns a string representation of the tree values.
    # Sorted with smallest value first
    def __str__(self):
        txt = "{ "
        if self.root is not None:
            txt += self.root.__str__()
        return txt + "}"

    # Count total number of nodes in the tree
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Number of nodes in longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Delete a node with value val from tree. Returns True if succesful
    # and False if value val doesn't exist in tree.
    # Extra care taken for removing the root.
    def delete(self, val):
        if self.root is None:  # Empty tree
            return False

        if self.root.value == val:  # Delete root
            if self.root.left is None:
                if self.root.right is None:  # Delete singleton
                    self.root = None
                    return True
                else:      # Case 1 for root
                    self.root = self.root.right  # Bypass root
        return self.root.delete(val, None)

    # Returns a string representing a DOT markup of
    # the BST suitable fror Graphvis Online.
    def dot(self):
        if self.root is None:
            return "No nodes ==> no graph markup"
        else:
            dot_text = "graph BST {\n"
            dot_text += self.root.dot(None)  # None as parent
            dot_text += "}"
            return dot_text
