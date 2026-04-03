class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x:int) -> None:
        self.q.append(x)

    def pop(self) -> None:
        for _ in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0

# class MyStack:

#     def __init__(self):
#         self.q = None

#     def push(self, x: int) -> None:
#         self.q = deque([x, self.q])

#     def pop(self) -> int:
#         top = self.q.popleft()
#         self.q = self.q.popleft()
#         return top

#     def top(self) -> int:
#         return self.q[0]

#     def empty(self) -> bool:
#         return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()