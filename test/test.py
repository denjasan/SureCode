import time


# k = 0
# for i in open('BM.py', 'r').readlines():
#     if '    ' in i:
#         k += 1
#     print(i[:-1])
# print(k)

# p = input()
# s = open('wow.txt', 'r').readlines()
# before = time.time()
# res = s.find(p)
# after = time.time()
# print(res, after - before)

# before = time.time()
# res = sum([len(i) for i in s])
# after = time.time()
# print(res, after - before)

def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")

print('mew')
