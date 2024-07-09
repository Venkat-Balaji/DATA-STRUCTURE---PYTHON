class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

head , tail =None,None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def create():
        global head , tail
        value=int(input())
        while value!=-1:
            newnode=Node(value)
            if head is None:
                head=newnode
                tail=newnode
            else:
                tail.next=newnode
                tail=newnode
            value=int(input())
    create()
    def display():
        global head
        temp=head
    
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
    display()




