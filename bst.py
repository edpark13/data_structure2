#! /usr/bin/env python

import random

class Node(object):
    def __init__(self, data, left=None, right=None, parent=None):
        """Creates a node for the Bst class"""
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def delete(self, key):
        """ delete the node with the given key and return the 
        root node of the tree """        
        if self.data == key:
            # found the node we need to delete
            if self.right and self.left: 
                # get the successor node and its parent 
                [psucc, succ] = self.right._findMin(self)
                # splice out the successor
                # (we need the parent to do this) 
                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right
                # reset the left and right children of the successor
                succ.left = self.left
                succ.right = self.right
                return succ                
            else:
                # "easier" case
                if self.left:
                    return self.left    # promote the left subtree
                else:
                    return self.right   # promote the right subtree 
        else:
            if self.data > key:          # key should be in the left subtree
                if self.left:
                    self.left = self.left.delete(key)
                # else the key is not in the tree 
            else:                       # key should be in the right subtree
                if self.right:
                    self.right = self.right.delete(key)
        return self
    
    def _findMin(self, parent):
        """ return the minimum node in the current tree and its parent """

        # we use an ugly trick: the parent node is passed in as an argument
        # so that eventually when the leftmost child is reached, the 
        # call can return both the parent to the successor and the successor
        
        if self.left:
            return self.left._findMin(self)
        else:
            return [parent, self]

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.data is None else (
            "\t%s;\n%s\n" % (
                self.data,
                "\n".join(self._get_dot())
            )
        ))

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.data, self.left.data)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.data, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.data, self.right.data)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.data, r)

class Bst(object):
    top = None
    def __init__(self):
        """Initialize a binary search tree"""
        self.top = None
        self.set = set()
        self.depth = 0
        self.dleft = 1
        self.dright = 1
        global top
        top = self.top

    def insert(self, val):
        """Insert a Node into the binary tree and tracks the
        depth of the right and left branches"""
        if val not in self.set:
            count = 1
            if not self.top:
                self.top = Node(val)
            else:
                current = self.top
                while current:
                    if val < current.data:
                        if current.left is None:
                            current.left = Node(val, parent=current)
                            break
                        current = current.left
                    else:
                        if current.right is None:
                            current.right = Node(val, parent=current)
                            break
                        current = current.right
                    count += 1
                count += 1
            if count > self.depth:
                self.depth = count
            if val < self.top.data and count > self.dleft:
                self.dleft = count
            elif val > self.dright and count > self.dright:
                self.dright = count
            self.set.add(val)

    def contains(self, val):
        """Return a boolean value if value currently exits in the tree"""
        return val in self.set

    def size(self):
        """Return the current number of items in the tree"""
        return len(self.set)

    def depth(self):
        """Return the depth of the longest branch"""
        return self.depth

    def balance(self):
        """Determines if the right is deeper than the left branch"""
        return self.dleft - self.dright

    def in_order(self):
        """Return a generator of the values using in order traversal"""
        l = self.in_order_helper(self.top, [])
        for num in l:
            yield num

    def in_order_helper(self, current, l):
        """With the top node iterativally call other nodes in order traversal"""
        if current:
            self.in_order_helper(current.left, l)
            l.append(current.data)
            self.in_order_helper(current.right, l)
        # yield current.data
        return l

    def pre_order(self):
        """Return a generator of the values using pre order traversal"""
        l = self.pre_order_helper(self.top, [])
        for num in l:
            yield num

    def pre_order_helper(self, current, l):
        """With the top node iterativally call other nodes pre order traversal"""
        if current:
            l.append(current.data)
            self.pre_order_helper(current.left, l)
            self.pre_order_helper(current.right, l)
        # yield current.data
        return l

    def post_order(self):
        """Return a generator of the values using post order traversal"""
        l = self.post_order_helper(self.top, [])
        for num in l:
            yield num

    def post_order_helper(self, current, l):
        """With the top node iterativally call other nodes post order traversal"""
        if current:
            self.post_order_helper(current.left, l)
            self.post_order_helper(current.right, l)
            l.append(current.data)
        # yield current.data
        return l
    def breadth_first(self):
        """Return a generator of the values using breadth first traversal"""
        q = []
        q.append(self.top)
        while q != []:
            node = q.pop(0)
            yield node.data
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
 
    def delete(self, value):
        """Remove a value from a tree and updates the tree with the correct
        values"""
        # if value not in self.set:
        #     return None
        # # find the node with the value
        # current = self.top
        # while current.data != value:
        #     if value < current.data:
        #         current = current.left
        #     else:
        #         current = current.right
        # # current = the value we passed in        
        # if current.left is None and current.right is None:
        #     if current.parent.data > current.data:
        #         current.parent.right = None
        #     else:
        #         current.parent.left = None
        # elif current.left is None:
        #     current.parent = current.right
        if self.top:
            self.top.delete(value)


if __name__ == '__main__':
    tree = Bst()
    tree.insert(5)
    tree.insert(7)
    tree.insert(8)
    tree.insert(6)
    tree.insert(9)
    tree.insert(3)
    tree.delete(7)
    import subprocess
    dot_graph = tree.top.get_dot()
    t = subprocess.Popen(["dot", "-Tpng"], stdin=subprocess.PIPE)
    t.communicate(dot_graph)
    #Because the search funtion uses a set look up the look up speed
    #will be a O(1)
