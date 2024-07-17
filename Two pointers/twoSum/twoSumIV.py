#Two Sum IV - Input into a BST
#Easy
#Two pointer implementation
#Problem: Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodes = []
        def inOrder(node): #Flatten out the tree
            if node == None:
                return
            inOrder(node.left)
            nodes.append(node.val)
            inOrder(node.right)
        inOrder(root)
        start = 0
        end = len(nodes) - 1
        while(start < end):
            if nodes[start] == None:
                start += 1
            elif nodes[end] == None:
                end -= 1
            nodeSum = nodes[start] + nodes[end]
            if nodeSum == k:
                return True
            elif nodeSum > k:
                end -= 1
            else:
                start += 1
        return False    
            