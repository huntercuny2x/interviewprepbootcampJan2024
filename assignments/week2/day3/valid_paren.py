def isValid(s):
    close_to_open={'}':'{', ']':'[', ')':'('}
    stack =[]

    for c in s:
        if c in close_to_open.values():
            stack.append(c)
        
        elif stack and stack[-1]==close_to_open[c]:
            stack.pop()
        
        else:
            return False
    return not stack