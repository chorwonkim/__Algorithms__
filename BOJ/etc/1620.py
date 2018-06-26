from sys import stdin, stdout
import bisect
Read = stdin.readline
Write = stdout.write


N, M = map(int, Read().split())
# pokemon_dict = {}
#
# for i in range(N):
#     pokemon_dict[i] = Read().rstrip()
#
# for _ in range(M):
#     question = Read().rstrip()
#
#     if question.isdigit():
#         # print(pokemon_dict[int(question)-1])
#         Write(pokemon_dict[int(question)-1] + "\n")
#     else:
#         result = [number for number, name in pokemon_dict.items() if question == name]
#         # print(result[0]+1)
#         Write(str(result[0]+1) + "\n")

pokedex = [Read().rstrip() for _ in range(N)]
pokedex_sort = sorted(pokedex)
pokenum = sorted([[pokedex[i], str(i+1)] for i in range(len(pokedex))], key=lambda x: x[0])

result = ""
#
# print(pokedex_sort)
# print(pokedex)
# print(pokenum)

for i in range(M):
    question = Read().rstrip()

    if question.isdigit():
        result += pokedex[int(question)-1] + '\n'
    else:
        result += pokenum[bisect.bisect(pokedex_sort, question)-1][1] + '\n'

print(result[:-1])