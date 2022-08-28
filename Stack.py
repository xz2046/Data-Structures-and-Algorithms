class Stack:
    def __init__(self, list=[]):
        self.stack = []
        for i in list:
            self.push(i)

    def isEmpty(self):
        return not self.stack

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if not self.stack:
            print("栈值为空")
        else:
            self.stack.pop()

    def top(self):
        if not self.stack:
            print("栈值为空")
        else:
            return self.stack[-1]

    def bottom(self):
        if not self.stack:
            print("栈值为空")
        else:
            return self.stack[0]

