class Parent:
    ParentAtrri=100
    def __init__(self):
        print("calling parent constructor")
    def parentMethod(self):
        print("Calling parent method")
    def setAttri(self,Attri):
        Parent.ParentAttri=Attri
        
    def getAttri(self):
        print("Parent Attribute:",Parent.ParentAttri)
        
    class Child(Parent):
        def __init__(self):
            print("calling parent constructor")
        
        def childMethod(self):
            print("Calling chhild method")
            
c=Child()
c.childMethod()
c.parentMethod()
c.setAttri(200)
c.getAttri()
            
        