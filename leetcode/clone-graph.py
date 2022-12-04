// https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def copyNode(node, nodes):
            if node.val not in nodes:
                nodes[node.val] = Node(node.val)
            return nodes[node.val]
        
        if node is None:
            return None
        
        queue = deque([node])
        visited = set()
        nodes = dict()
        
        while queue:
            cur = queue.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            cur_copy = copyNode(cur, nodes)
            
            for neighbor in cur.neighbors:
                cur_copy.neighbors.append(copyNode(neighbor, nodes))
            
            queue.extend(cur.neighbors)
        
        return nodes[node.val]