def valid_parentheses(string):
    lst = []
    for i, val in enumerate(string):
        if val == '(' or val == ')':
            lst.append((i, val))
    print(lst)
print(valid_parentheses("()(())test"))