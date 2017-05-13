# [4.2] Minimal Tree: Given a sorted(increasing order)
# array with unique integer elements, write an algorithm
# to create a binary search tree with minimal height

# Space complexity:
# Time complexity:


import unittest

class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def minTree(nums):
  # Edge Case
  if not nums:
    return None

  mid = len(nums)/2
  root = TreeNode(nums[mid])
  root.left = minTree(nums[:mid])
  root.right = minTree(nums[mid+1:])

  return root


class Test(unittest.TestCase):
    def test_minTree(self):
        bst = minTree([2,3,4,5,6,7])
        self.assertEqual(bst.value, 5)
        self.assertEqual(bst.left.value, 3)
        self.assertEqual(bst.left.left.value, 2)
        self.assertEqual(bst.left.right.value, 4)
        self.assertEqual(bst.right.value, 7)
        self.assertEqual(bst.right.left.value, 6)

if __name__ == '__main__':
    unittest.main()
