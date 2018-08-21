from itertools import permutations

S = list(input())
character_dict = {}
count = 0

for item in S:
    if item in character_dict:
        continue
    else:
        character_dict[item] = S.count(item)

for items in permutations(S):
    temp = ''.join(items)

    # if temp in trial_checker:
    #     if trial_checker[temp]:
    #         continue
    #     else:
    #         continue
    # else:
    #     trial_checker[temp] = False
    #
    #     for i in range(1, len(temp)-1):
    #         if temp[i] == temp[i-1] or temp[i] == temp[i+1]:
    #             trial_checker[temp] = True
    #             break
    #
    #     if not trial_checker[temp]:
    #         count += 1

    string_checker = False

    for i in range(1, len(temp) - 1):
        if temp[i] == temp[i - 1] or temp[i] == temp[i + 1]:
            string_checker = True
            break

    if not string_checker:
        count += 1


for i in character_dict:
    # print(character_dict[i])
    overlapping = 1
    for j in range(1, character_dict[i]+1):
        overlapping *= j

    count = count // overlapping

print(count)