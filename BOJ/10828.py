def top(stack):
    if not stack:
        return -1
    else:
        temp = stack.pop()
        stack.append(temp)
        return temp


implement_stack = []
for i in range(int(input())):
    order = input()

    if "push" in order:
        x, y = order.split()
        implement_stack.append(int(y))
    elif "top" in order:
        print(top(implement_stack))
    elif "size" in order:
        print(len(implement_stack))
    elif "empty" in order:
        if not implement_stack:
            print(1)
        else:
            print(0)
    elif "pop" in order:
        if not implement_stack:
            print(-1)
        else:
            print(implement_stack.pop())
