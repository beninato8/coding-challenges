class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedToOpen = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if len(stack) == 0:
                if c in closedToOpen:
                    return False
                stack.append(c) 
            else:
                top = stack[-1]
                if c in closedToOpen:
                    if closedToOpen[c] != top:
                        return False
                    else:
                        stack.pop() 
                else:
                    stack.append(c) 
            
        return len(stack) == 0
