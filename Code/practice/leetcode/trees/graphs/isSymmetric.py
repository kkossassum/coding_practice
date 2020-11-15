# *********************************************
# Source : https://oj.leetcode.com/problems/symmetric-tree/
# Author : wizcabbit
# Date   : 2014-11-03

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# *********************************************

# Recursively Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
    

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:




if __name__ == '__main__':
    """case 1"""
    a = TreeNode(1)

    b1 = TreeNode(2)
    b2 = TreeNode(2)

    c1 = TreeNode(3)
    c2 = TreeNode(4)
    c3 = TreeNode(4)
    c4 = TreeNode(3)

    a.left = b1
    a.right = b2
    b1.left = c1
    b1.right = c2
    b2.left = c3
    b2.right = c4

    """case 2"""
    a = TreeNode(1)
    
    b1 = TreeNode(2)
    b2 = TreeNode(2)
    
    c1 = TreeNode(3)
    c2 = TreeNode(3)
    
    a.left = b1
    a.right = b2
    b1.right = c1
    b2.right = c2

    print(Solution().isSymmetric(a))