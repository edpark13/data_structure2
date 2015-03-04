import random

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Bst(object):
    def __init__(self):
        self.top = None
        self.list = []
        self.depth = 0
        self.dleft = 1
        self.dright = 1

    def insert(self, val):
        if not val in self.list:
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
                    elif val > current.data:
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
            self.list.append(val)

    def contains(self, val):
        return val in self.list

    def size(self):
        return len(self.list)

    def depth(self):
        return self.depth

    def balance(self):
        return self.dright - self.dleft

    def get_dot(self):
        """return the tree with root 'self' as a dot graph for visualization"""
        return "digraph G{\n%s}" % ("" if self.top is None else (
            "\t%s;\n%s\n" % (
                self.top,
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


if __name__ == '__main__':
    tree = Bst()
    tree.insert(5)
    tree.insert(7)
    tree.insert(8)
    tree.insert(6)
    tree.insert(9)
    tree.insert(3)
    tree.get_dot()

