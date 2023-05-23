pars = {")": "(", "]": "[", '}': '{'}


def par_checker_mod(string):
    stack = []

    for s in string:
        if s in "([{":
            stack.append(s)
        elif s in ")]}":
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

string = '{[]()}'
print(par_checker_mod(string))
