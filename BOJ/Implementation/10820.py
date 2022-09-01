while True:
    try:
        result = [0 for _ in range(4)]
        data = input()

        for i in data:
            if 'A' <= i <= 'Z':
                result[1] += 1
            elif 'a' <= i <= 'z':
                result[0] += 1
            elif '0' <= i <= '9':
                result[2] += 1
            elif i == ' ':
                result[3] += 1

        for i in result:
            print(i, end=' ')
    except EOFError:
        break