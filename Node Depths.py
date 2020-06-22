# ####DANGER! WHILE LOOP IN PROGRESS!!!
# def iterativeNodeDepths(root):
#     sumOfDepths = 0
#     stack = [{"node": root[0][0]["id"], "depth": 0}]
#     print(stack)
#     while len(stack) > 0:
#         nodeInfo = stack.pop()
#         node, depth = nodeInfo["node"], nodeInfo["depth"]
#         print(stack)
#         if node is None:
#             continue
#         sumOfDepths += depth
#         stack.append({"node": root[0][0]["left"], "depth": depth + 1})
#         stack.append({"node": root[0][0]["right"], "depth": depth + 1})
#     return sumOfDepths

# def nodeDepths(root, depth=0):
#     if root is None:
#         return
#     return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


# nodes = [{"id": "1", "left": "2", "right": "3", "value": 1},
#          {"id": "2", "left": "4", "right": "5", "value": 2},
#          {"id": "3", "left": "6", "right": "7", "value": 3},
#          {"id": "4", "left": "8", "right": "9", "value": 4},
#          {"id": "5", "left": None, "right": None, "value": 5},
#          {"id": "6", "left": None, "right": None, "value": 6},
#          {"id": "7", "left": None, "right": None, "value": 7},
#          {"id": "8", "left": None, "right": None, "value": 8},
#          {"id": "9", "left": None, "right": None, "value": 9}
#          ],
# print(iterativeNodeDepths(nodes))



def nodeDepths(root):
	sumOfDepths = 0
	stack = [{"node": root, "depth": 0}]
	while len(stack) > 0:
		nodeInfo = stack.pop()
		node, depth = nodeInfo["node"], nodeInfo["depth"]
		if node is None:
			continue
		sumOfDepths += depth
		stack.append({"node": node.left, "depth": depth + 1})
		stack.append({"node": node.right, "depth": depth + 1})

	return sumOfDepths

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
test = {
    "nodes": [
      {"id": "1", "left": "2", "right": "3", "value": 1},
      {"id": "2", "left": "4", "right": "5", "value": 2},
      {"id": "3", "left": "6", "right": "7", "value": 3},
      {"id": "4", "left": "8", "right": "9", "value": 4},
      {"id": "5", "left": None, "right": None, "value": 5},
      {"id": "6", "left": None, "right": None, "value": 6},
      {"id": "7", "left": None, "right": None, "value": 7},
      {"id": "8", "left": None, "right": None, "value": 8},
      {"id": "9", "left": None, "right": None, "value": 9}
    ],
    "root": "1"
  }
print(test["nodes"][2]["left"])