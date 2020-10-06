class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
    
class sLinkedList:
    def __init__(self):
        self.headval=None
    def InBetween(self,MiddleNode,Newdata):
        if MiddleNode is None:
            print("The node is missing")
            return
        NewNode=Node(Newdata)
        NewNode.nextval=MiddleNode.nextval
        MiddleNode.nextval=NewNode
    """def AtEnd(self,newnode):
        Newdata=Node(newnode)
        e3.nextval=Newdata"""
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
    
    """def AtBegining(self,newdata):
        newnode=Node(newdata)
        
        newnode.nextval=self.headval
        self.headval=newnode"""
        

list=sLinkedList()
list.headval=Node("Monday")
e2=Node("Thuesday")
e3=Node("Wednesday")

list.headval.nextval=e2
e2.nextval=e3
#list.AtBegining("Sunday")
#list.AtEnd("Thursday")
list.InBetween(list.headval.nextval,"Friday")
list.listprint()
            