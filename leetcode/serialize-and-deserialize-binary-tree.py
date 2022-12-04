// https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def dfs(node = root, index = 0, nodeDict = dict()):
            if not node:
                return
            
            nodeDict[index] = node.val
            dfs(node.left, index * 2 + 1, nodeDict)
            dfs(node.right, index * 2 + 2, nodeDict)
            
            return nodeDict

        nodeDict = dfs()
        if nodeDict:
            return ','.join([str(k) + ":" + str(v) for k,v in nodeDict.items()])
        else:
            return ''

        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def dfs(index = 0):
            
            if index not in nodeDict:
                return None
            
            node = TreeNode(nodeDict[index])
            node.left = dfs(index * 2 + 1)
            node.right = dfs(index * 2 + 2)
            return node
        
        if not data:
            return None
        
        nodeDict = dict()
        for item in data.split(','):
            k,v = item.split(':')
            nodeDict[int(k)] = int(v)
        
        return dfs()
        

        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))