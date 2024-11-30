# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        return inorder(root)

#inorder means first go left, then process node, then go right
#understanding: We are given a root of a binary tree, we need to return an array of the values by using inorder traversal 
#match: binary tree problem, in order traversal problem
#plan: implement inorder traversal, check if node is not valid, if not return, if yes traverse to node.left, add node value to array, traverse node.righ, add the return call in a left + [node] + right fashion
