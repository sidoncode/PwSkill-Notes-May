class parent:
    def parent(self):
        print("Parent Method")

class child1(parent):
    def child1(self):
        print("Child1 Method")
        super().parent()

class child2(parent):
    def child2(self):
        print("Child2 Method")

obj_child1 = child1()
obj_child1.child1()