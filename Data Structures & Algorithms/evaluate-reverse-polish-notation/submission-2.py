class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for i in tokens:
            if (i!="+" and i!="-" and i!="/" and i!="*"):
                stack.append(int(i))
            else:
                if i =="+":
                    x = stack.pop()
                    y = stack.pop()
                    res = y + x
                    stack.append(res)
                if i =="-":
                    x = stack.pop()
                    y = stack.pop()
                    res = y - x
                    stack.append(res)
                if i =="*":
                    x = stack.pop()
                    y = stack.pop()
                    res = y * x
                    stack.append(res)
                if i =="/":
                    x = stack.pop()
                    y = stack.pop()
                    res = int(y / x)
                    stack.append(res)
        return stack.pop()
                

        