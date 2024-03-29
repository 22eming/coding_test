N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]


def pre(root):
    if root != '.':
        print(root, end='')
        pre(tree[root][0])
        pre(tree[root][1])


def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])


def post(root):
    if root != ".":
        post(tree[root][0])
        post(tree[root][1])
        print(root, end='')


for traversal in [pre, inorder, post]:
    traversal('A')
    print()