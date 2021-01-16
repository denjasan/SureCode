# import time
# import re
#
#
# k = 0
# for i in open('BM.py', 'r').readlines():
#     if '    ' in i:
#         k += 1
#     print(i[:-1])
# print(k)
#
# p = input()
# s = open('wow.txt', 'r').readlines()
# before = time.time()
# res = 'kek'
# after = time.time()
# print(res, after - before)
#
# before = time.time()
# res = sum([len(i) for i in s])
# after = time.time()
# print(res, after - before)
#
#
# def my_function(**kid):
#     print("His last name is " + kid["lname"])
#
#
# my_function(fname="Tobias", lname="Refsnes")
#
# print('mew'
#       + 'gav'
#       + 'sex')
#
# print(re.search(r'k\wa', r'kia')[0])

print('^800)))9(&%s'.lower())
print('^800)))9(&%s'.upper())


def sql_injection(self):
    """ ru: SQLi уязвимость
    en: SQLi vulnerability """
    can = {
        'select': {'new_line': True, 'begin': 'execute(', 'end': ")",
                   'elements': ['%s', '" +', "' +", '""" +', '"+', "'+", '"""+', 'f"', "f'"]}
    }
    lines_list = self.search(what='select', case=True, new_line=can['select']['new_line'],
                             begin=can['select']['begin'], end=can['select']['end'])

    res = []
    for lines in lines_list:
        for elem in can['select']['elements']:
            if any([elem in self.file_lines[line - 1] for line in lines]):
                res.append(lines)
    return res

