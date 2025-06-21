class Grandparent:
    def grandFunction(self):
        print("GrandParent Method")

class parent(Grandparent):
    def parentfunction(self):
        print("Parent Method")

class child(parent):
    def childfunction(self):
        print("Child Method")

obj_child = child()
obj_child.grandFunction()
obj_child.parentfunction()
obj_child.childfunction()