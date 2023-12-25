from Stack import Stack

def bracket_check(test_string):
    isError = False
    position = []
    location = []
    stack = Stack()

    for i in range(len(test_string)):
        s = test_string[i]
        if s == '(' or s == '[' or s == '{':
            stack.push(s)
            position.append(i)
        elif s == ')' or s == ']' or s == '}':
            p = ''

            #if not stack.isEmpty():
            #    isError = True
            #    location.append(i)

            if not stack.isEmpty():
                p = stack.pop()
                position.append(i)
            else:
                isError = True

            if ((p == '(' and s == ')') or
                (p == '[' and s == ']') or
                (p == '{' and s == '}')):
                #isError = False
                position.pop(len(position)-1)
                position.pop(len(position)-1)
                #position = []
                p = ''
                s = ''
            else:
                isError = True
                location = position

    #while not stack.isEmpty():
    #    isError = True
    #    location.append(i)

    if not stack.isEmpty():
        isError = True
        location = position



    return isError, location
