def branchSums(root):
    return recursiveHelper(root, 0, [])


def recursiveHelper(node, runningSum, array):
    if node is None:
        return

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        array.append(newRunningSum)
        return
    
    recursiveHelper(node.left, newRunningSum, array)
    recursiveHelper(node.right, newRunningSum, array)
    return array