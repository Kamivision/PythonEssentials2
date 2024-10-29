class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        self.__stack_list = [] # Creating hidden property.

    def push(self, val): # Defining push function
        self.__stack_list.append(val) 


    def pop(self): # Defining pop function
        val = self.__stack_list[-1]
        del self.__stack_list[-1] 
        return val

class AddingStack(Stack):   # Defining subclass of Stack class.
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

     def get_sum(self):  # Defining method to provide value of __sum
        return self.__sum

    def push(self, val):    # Redefining push() for subclass
        self.__sum += val
        Stack.push(self, val)

    def pop(self):  # Redefining pop() for subclass
        val = Stack.pop(self)
        self.__sum -= val
        return val

stack_object = Stack()  # Instantiating the object.

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())











# stack_object.push(3)    # Using push()
# stack_object.push(2)
# stack_object.push(1)

# print(stack_object.pop())   # Using pop()
# print(stack_object.pop())
# print(stack_object.pop())



