#ex1
# list1 = [1, 2, 3, 4, 5]
# a  = list(map(lambda x: x * 2, list1))
# print(a)


#ex2
# s = str(input())
# lc = list(filter(lambda x: (x.islower()), s))
# uc = list(filter(lambda x: (x.isupper()), s))
# print(len(lc), len(uc))


#ex3
# s = str(input())
# r = ''.join(reversed(s))
# print(r)
# if (s == r):
#     print(True)
# else:
#     print(False)


#ex4
# from time import sleep
# import math
# n = int(input())
# seconds = int(input())
# sq = math.sqrt(n)
# sleep(seconds / 1000)
# print(f"Square root of", n, f"after {seconds} miliseconds is", sq)


#ex5
# x = tuple((1 + 1 == 2, 4 / 2 == 2, True))
# if len(x) == sum(x):
#     print(True)
# else:
#     print(False)
        