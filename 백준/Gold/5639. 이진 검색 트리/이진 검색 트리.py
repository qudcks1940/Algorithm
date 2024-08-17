# 전위순회의 결과를 보고
# 트리의 구조를 예측한 다음
# 그 트리로 다시 후위순회의 결과를 꺼내면 될 거 같다.
# 전위순회의 결과를 보고
# 어떻게 트리의 구조를 예측할 것인가를 생각중.
# 1. 일단 left노드의 값이 right 노드의 값보다 항상 커야한다.
# 전위 순회는 mid left right 순이기 때문에
# 첫 번째 값이 무조건 root이다.

import sys
input=sys.stdin.read
sys.setrecursionlimit(10**6)
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def insert(node, value):
    




# def postorder(node):
#     if node.left:
#         postorder(node.left)
#     if node.right:
#         postorder(node.right)
#     print(node.value)

# root = Node(preorder_result[0])

# for value in preorder_result[1:]:
#     insert(root, value)

# postorder(root)
    

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(preorder, start, end):
    if start > end:
        return None

    # 첫 번째 값이 루트가 됨
    root = Node(preorder[start])

    # 오른쪽 서브트리가 시작되는 지점을 찾음
    idx = start + 1
    while idx <= end and preorder[idx] < root.value:
        idx += 1

    # 왼쪽 서브트리와 오른쪽 서브트리를 재귀적으로 구성
    root.left = build_tree(preorder, start + 1, idx - 1)
    root.right = build_tree(preorder, idx, end)

    return root

def print_tree_inorder(node):
    if node.left:
        print_tree_inorder(node.left)
    print(node.value, end=" ")
    if node.right:
        print_tree_inorder(node.right)

def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.value)

preorder_input = []
while True:
    try:
        preorder_input.append(int(sys.stdin.readline().strip()))
    except:
        break
# 입력값

# 트리 구성
root = build_tree(preorder_input, 0, len(preorder_input) - 1)

# 결과 출력 (후위 순회)
postorder(root)
