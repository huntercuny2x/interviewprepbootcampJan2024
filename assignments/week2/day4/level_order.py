import collections

def levelOrder(root):
    q = collections.deque()
    if root:
        q.append(root)
    
    level_order=[]

    while q:
        level=[]
        for i in range(len(q)):
            node=q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level_order.append(level)
    
    return level_order