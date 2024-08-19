# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def inOrder(root):
            if root is None:
                return []
            
            return inOrder(root.left) + [root.val] + inOrder(root.right)
        lst = inOrder(root)
        start = 0
        end = len(lst) - 1
        while(start < end):
            sum_num = lst[start] + lst[end]
            if sum_num == k:
                return True
            elif sum_num > k:
                end -= 1
            else:
                start += 1
        return False
    