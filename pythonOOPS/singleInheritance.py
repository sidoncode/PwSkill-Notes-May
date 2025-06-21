class parent:
    def show(self):
        print("Parent Method")

class child(parent):
    def show(self):
        print("Hello from Child class")

# creating an object(callable property) -> context(parent class)
obj_parent = parent()
obj_parent.show()

# creting a object in the context of child class
obj_child = child()
obj_child.show()