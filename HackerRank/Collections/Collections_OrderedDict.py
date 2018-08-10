from collections import OrderedDict

dictionary = OrderedDict()

for _ in range(int(input())):
    item_name, *args, price = input().split()

    if args:
        item_name = item_name + " " + ''.join(args)

    if item_name in dictionary.keys():
        dictionary[item_name] += int(price)
    else:
        dictionary[item_name] = int(price)

for k, v in dictionary.items():
    print(k, v)
