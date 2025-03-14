class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins:
            self.mins.append(val)
        elif val < self.mins[-1]:
            self.mins.append(val)
        else: self.mins.append(self.mins[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.mins:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]



    def getMin(self) -> int:
        return self.mins[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.pop()
    obj.push(4)
    print(obj.getMin())
    print(obj.top())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
