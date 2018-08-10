def merge_the_tools(string, k):
    # your code goes here
    temp = ''
    count = 0
    for item in string:
        count += 1
        if not temp.count(item):
            temp += item

        if count == k:
            print(temp)
            count = 0
            temp = ''


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)