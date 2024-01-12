def maxDepthRecursive(root):
    if not root:
        return 0
    
    else:
        return max(maxDepthRecursive(root.left), maxDepthRecursive(root.right))+1


def maxDepthIterative(root):
    max_depth=0
    stack=[]
    if root:
        stack=[[root,1]]
    
    while stack:
        node, count = stack.pop()
        if node:
            if node.left:
                stack.append([node.left, count+1])
            if node.right:
                stack.append([node.right, count+1])
            max_depth=max(max_depth,count)

    return max_depth