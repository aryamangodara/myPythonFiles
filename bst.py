#Binary_Search_Tree
class Node:
    left,right,data=None,None,None
    
head=Node()

def add(element):
    temp=head
    if temp.data==None:
        temp.data=element
    
    else:
        while True:
            if element>temp.data:
                if temp.right==None:
                    temp2 = Node()
                    temp2.data = element
                    temp.right=temp2
                    break
                else:
                    temp=temp.right
            else:
                if temp.left==None:
                    temp2 = Node()
                    temp2.data = element
                    temp.left=temp2
                    break
                else:
                    temp=temp.left

a=[15,17,10,16,19,11,12,1,11,2]
for i in a:
    add(i)

# print(head.right.data)
def search(item):
    global head
    result=True
    temp=head
    while result:
        if temp==None:
            result=False
        elif item==temp.data:
            break
        elif item>temp.data:
            temp=temp.right
        else:
            temp=temp.left
    
    return result
    
print(search(12))
def preorder(node):
    # global head
    if node==None:
        return
    preorder(node.left)
    print(node.data)
    preorder(node.right)


preorder(head)
print("\n")
def postorder(node):
    if node==None:
        return
    postorder(node.right)
    print(node.data)
    postorder(node.left)


postorder(head)

print("\n")
def inorder(node):
    if node:
        inorder(node.right)
        inorder(node.left)
        print(node.data)
        
        
inorder(head)















