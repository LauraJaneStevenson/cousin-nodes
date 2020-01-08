class Node(object):
    """Doubly-linked node in a tree.

        >>> na = Node("na")
        >>> nb1 = Node("nb1")
        >>> nb2 = Node("nb2")

        >>> nb1.set_parent(na)
        >>> nb2.set_parent(na)

        >>> na.children
        [<Node nb1>, <Node nb2>]

        >>> nb1.parent
        <Node na>
    """

    parent = None

    def __init__(self, data):
        self.children = []
        self.data = data

    def __repr__(self):
        return "<Node %s>" % self.data

    def set_parent(self, parent):
        """Set parent of this node.

        Also sets the children of the parent to include this node.
        """

        self.parent = parent
        parent.children.append(self)

    def cousins(self):
        """Find nodes on the same level as this node."""

        # create set of parent nodes children
        cs = set(self.parent.children)

        # remove this node from set
        cs.remove(self)

        # return set
        return cs




na = Node("na")
nb1 = Node("nb1")
nb2 = Node("nb2")
nb3 = Node("nb3")

nb1.set_parent(na)
nb2.set_parent(na)
nb3.set_parent(na)

