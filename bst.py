#! /usr/bin/env python

import random

class Node(object):
    def __init__(self, data, left=None, right=None):
        """Creates a node for the Bst class"""
        self.data = data
        self.left = left
        self.right = right

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
    def __init__(self):
        """Initialize a binary search tree"""
        self.top = None
        self.set = set()
        self.depth = 0
        self.dleft = 1
        self.dright = 1

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
                            current.left = Node(val)
                            break
                        current = current.left
                    else:
                        if current.right is None:
                            current.right = Node(val)
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
        l = self.in_order_helper(self.top, [])
        for num in l:
            yield num

    def in_order_helper(self, current, l):
        if current:
            self.in_order_helper(current.left, l)
            l.append(current.data)
            self.in_order_helper(current.right, l)
        # yield current.data
        return l
    def pre_order(self):
        pass

    def post_order(self):
        pass

    def breadth_first(self):
        pass


if __name__ == '__main__':
    tree = Bst()
    tree.insert(5)
    tree.insert(7)
    tree.insert(8)
    tree.insert(6)
    tree.insert(9)
    tree.insert(3)
    import subprocess
    dot_graph = tree.top.get_dot()
    t = subprocess.Popen(["dot", "-Tpng"], stdin=subprocess.PIPE)
    t.communicate(dot_graph)
    #Because the search funtion uses a set look up the look up speed
    #will be a O(1)
