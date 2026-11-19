class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def traversal(node1):
    currentnode=node1
    while currentnode:
        print(currentnode.data,end="->")
        currentnode=currentnode.next
    print("None")
node1=Node(13)
node2=Node(20)
node3=Node(50)
node1.next=node2
node2.next=node3
traversal(node1)