class Node:

    treenodes = []

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        Node.treenodes.append(self)

    def __repr__(self):
        return f"Node({self.data})"

    
def preorder(node,dataset):

    if node is None:
        return dataset
    
    stack = []
    current = node

    while current is not None or len(stack) > 0:

        while current is not None:

            stack.append(current)
            dataset.append(current.data)
            current = current.left

        current = stack.pop()
        current = current.right

    return dataset

def inorder(node,dataset):

    if node is None:
        return dataset

    stack = []
    curr = node

    while curr is not None or len(stack) > 0:

        while curr is not None:

            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        dataset.append(curr.data)
        curr = curr.right

    return dataset


def postorder(node,dataset):

    if node is None:
        return dataset

    curr = node
    stack = []
    lastvisitednode = None

    while curr is not None or len(stack) > 0:

        while curr is not None:
            stack.append(curr)
            curr = curr.left

        peeknode = stack[-1]

        if peeknode.right is not None and lastvisitednode != peeknode.right:
            curr = peeknode.right

        else:

            curr = stack.pop()
            dataset.append(curr.data)
            lastvisitednode = curr
            curr = None

    return dataset

def create():

    nodeval = int(input("Enter value for node (-1 for None)\n:"))

    if nodeval == -1:
        return

    root = Node(nodeval)

    print(f"Enter left value of {nodeval}")
    root.left = create()

    print(f"Enter right value of {nodeval}")
    root.right = create()

    return root


def main():

    head = create()

    print(f"Tree Nodes: {Node.treenodes}")

    preorderset = []
    preorder(head,preorderset)

    inorderset = []
    inorder(head,inorderset)

    postorderset = []
    postorder(head,postorderset)

    print(f"Pre: {preorderset}")

    print(f"In: {inorderset}")

    print(f"Post: {postorderset}")


main()