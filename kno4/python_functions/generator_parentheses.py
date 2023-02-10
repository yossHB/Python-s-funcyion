def valid_parentheses(combinition):
    stack = []
    for p in combinition:
        if p == '(':
            stack.append(p)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        return len(stack) == 0

def generate_stack(n):
    combs = []
    rec(2*n, 0,[],combs)
    return combs

def rec(n, diff,comb,combs):
    if diff < 0 or diff > n:
        return
    elif n == 0:
        if diff == 0:
            combs.append(''.join(comb))
    else:
        comb.append('(')
        rec(n-1, diff+1,comb,combs)
        comb.pop()
        comb.append(')')
        rec(n-1, diff-1,comb,combs)
        comb.pop()
