N = int(input())

for i in range(1, N+1):
    head = int(input())
    actions = input()

    for action in actions:
        if action is 'c':
            head += 1
        elif action is 'b':
            head -= 1

    print("Data Set %d:" % i)

    # Problems in output format, and don't know..
    if i == N:
        print(head)
    else:
        print(head, end='\n')

    if head <= 0:
        break;