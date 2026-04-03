class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            # If it's an opening bracket, add it to the stack
            if char in "({[":
                stack.append(char)
            # If it's a closing bracket, check for a match
            elif char == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack and stack[-1] == '[':
                stack.pop()
            # If it's a closing bracket with no match, it's invalid
            else:
                return False

        return len(stack) == 0