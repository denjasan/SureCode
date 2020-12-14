import time


# k = 0
# for i in open('BM.py', 'r').readlines():
#     if '    ' in i:
#         k += 1
#     print(i[:-1])
# print(k)

p, s = input(), open('wow.txt', 'r').readline()
before = time.time()
res = s.find(p)
after = time.time()
print(res, after - before)

