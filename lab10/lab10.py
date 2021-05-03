from unittest import TestCase
import random

class AVLTree:
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

        def rotate_right(self):
            n = self.left
            self.val, n.val = n.val, self.val
            self.left, n.left, self.right, n.right = n.left, n.right, n, self.right

        def rotate_left(self):
            n = self.right
            self.val, n.val = n.val, self.val
            self.right, n.right, self.left, n.left = n.right, n.left, n, self.left

        @staticmethod
        def height(n):
            if not n:
                return 0
            else:
                return max(1+AVLTree.Node.height(n.left), 1+AVLTree.Node.height(n.right))

    def __init__(self):
        self.size = 0
        self.root = None

    @staticmethod
    def balance_factor(node):
        if node == None:
            return 1
        else:
            lefth = AVLTree.height_rec(node.left)
            righth = AVLTree.height_rec(node.right)
            return lefth - righth

    @staticmethod
    def rebalance(t):
        ### BEGIN SOLUTION

        if t:
            bf = AVLTree.balance_factor(t)
            if bf > 1: # left heavy
                bf_inner = AVLTree.balance_factor(t.left)
                if bf_inner < 0:
                    t.left.rotate_left()
                t.rotate_right()
            elif bf < -1: # left heavy
                bf_inner = AVLTree.balance_factor(t.right)
                if bf_inner > 0:
                    t.right.rotate_right()
                t.rotate_left()

        ### END SOLUTION

    def add(self, val): # need to redo balance
        
        ### BEGIN SOLUTION
        def add_rec(node, val):
            if not node:
                return AVLTree.Node(val)
            elif val < node.val:
                left = add_rec(node.left, val)
                node.left = left
                AVLTree.rebalance(node)
                return node
            elif val > node.val:
                right = add_rec(node.right, val)
                node.right = right
                AVLTree.rebalance(node)
                return node

        assert(val not in self)

        self.root = add_rec(self.root, val)
        self.size += 1
        ### END SOLUTION

    def __delitem__(self, val): # need to redo balance
        
        ### BEGIN SOLUTION
        def rec_del(node, val):
            if not node:
                return node
            elif val < node.val:
                node.left = rec_del(node.left, val)
                return node
            elif val > node.val:
                node.right = rec_del(node.right, val)
                return node
            else:
                if not node.left and not node.right:
                    return None
                elif not node.left:
                    temp = node.right
                    node = None
                    AVLTree.rebalance(temp)
                    return temp
                elif not node.right:
                    temp = node.left
                    node = None
                    AVLTree.rebalance(temp)
                    return temp
                else:
                    temp = minval(node.right)
                    if temp:
                        node.val = temp.val
                        node.right = rec_del(node.right, temp.val)
                        return node
                    else:
                        return temp

        def minval(node):
            while node.left:
                node = node.left
            return node
        
        root = rec_del(self.root, val)
        self.size += -1

        ### END SOLUTION

    def __contains__(self, val):
        def contains_rec(node):
            if not node:
                return False
            elif val < node.val:
                return contains_rec(node.left)
            elif val > node.val:
                return contains_rec(node.right)
            else:
                return True
        return contains_rec(self.root)

    def __len__(self):
        return self.size

    def __iter__(self):
        def iter_rec(node):
            if node:
                yield from iter_rec(node.left)
                yield node.val
                yield from iter_rec(node.right)
        yield from iter_rec(self.root)

    def pprint(self, width=64):
        """Attempts to pretty-print this tree's contents."""
        height = self.height()
        nodes  = [(self.root, 0)]
        prev_level = 0
        repr_str = ''
        while nodes:
            n,level = nodes.pop(0)
            if prev_level != level:
                prev_level = level
                repr_str += '\n'
            if not n:
                if level < height-1:
                    nodes.extend([(None, level+1), (None, level+1)])
                repr_str += '{val:^{width}}'.format(val='-', width=width//2**level)
            elif n:
                if n.left or level < height-1:
                    nodes.append((n.left, level+1))
                if n.right or level < height-1:
                    nodes.append((n.right, level+1))
                repr_str += '{val:^{width}}'.format(val=n.val, width=width//2**level)
        print(repr_str)

    @staticmethod
    def height_rec(t):
            if not t:
                return 0
            else:
                return max(1+AVLTree.height_rec(t.left), 1+AVLTree.height_rec(t.right))

    def height(self):
        """Returns the height of the longest branch of the tree."""
        return self.height_rec(self.root)

################################################################################
# TEST CASES
################################################################################
def height(t):
    if not t:
        return 0
    else:
        return max(1+height(t.left), 1+height(t.right))

def traverse(t, fn):
    if t:
        fn(t)
        traverse(t.left, fn)
        traverse(t.right, fn)

# LL-fix (simple) test
# 10 points
def test_ll_fix_simple():
    tc = TestCase()
    t = AVLTree()

    for x in [3, 2, 1]:
        t.add(x)

    tc.assertEqual(height(t.root), 2)
    tc.assertEqual([t.root.left.val, t.root.val, t.root.right.val], [1, 2, 3])

# RR-fix (simple) test
# 10 points
def test_rr_fix_simple():
    tc = TestCase()
    t = AVLTree()

    for x in [1, 2, 3]:
        t.add(x)

    tc.assertEqual(height(t.root), 2)
    tc.assertEqual([t.root.left.val, t.root.val, t.root.right.val], [1, 2, 3])

# LR-fix (simple) test
# 10 points
def test_lr_fix_simple():
    tc = TestCase()
    t = AVLTree()

    for x in [3, 1, 2]:
        t.add(x)

    tc.assertEqual(height(t.root), 2)
    tc.assertEqual([t.root.left.val, t.root.val, t.root.right.val], [1, 2, 3])

# RL-fix (simple) test
# 10 points
def test_rl_fix_simple():
    tc = TestCase()
    t = AVLTree()

    for x in [1, 3, 2]:
        t.add(x)

    tc.assertEqual(height(t.root), 2)
    tc.assertEqual([t.root.left.val, t.root.val, t.root.right.val], [1, 2, 3])

# ensure key order is maintained after insertions and removals
# 30 points
def test_key_order_after_ops():
    tc = TestCase()
    vals = list(range(0, 50, 1))
    random.shuffle(vals)

    t = AVLTree()
    for x in vals:
        t.add(x)

    t.pprint()

    for _ in range(len(vals) //3):
        to_rem = vals.pop(random.randrange(len(vals)))
        del t[to_rem]
        #print("-----------------------")
        #t.pprint()

    vals.sort()

    for i,val in enumerate(t):
        tc.assertEqual(val, vals[i])

# stress testing
# 30 points
def test_stress_testing():
    tc = TestCase()

    def check_balance(t):
        tc.assertLess(abs(height(t.left) - height(t.right)), 2, 'Tree is out of balance')

    t = AVLTree()
    vals = list(range(1000))
    random.shuffle(vals)
    for i in range(len(vals)):
        t.add(vals[i])
        for x in vals[:i+1]:
            tc.assertIn(x, t, 'Element added not in tree')
        traverse(t.root, check_balance)

    random.shuffle(vals)
    for i in range(len(vals)):
        del t[vals[i]]
        for x in vals[i+1:]:
            tc.assertIn(x, t, 'Incorrect element removed from tree')
        for x in vals[:i+1]:
            tc.assertNotIn(x, t, 'Element removed still in tree')
        traverse(t.root, check_balance)



################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_ll_fix_simple,
              test_rr_fix_simple,
              test_lr_fix_simple,
              test_rl_fix_simple,
              test_key_order_after_ops,
              test_stress_testing]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
