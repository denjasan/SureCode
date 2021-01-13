# encoding: utf-8
# ru: тут основные функции поиска вредоносных элементов кода
# en: here are the main functions for searching for malicious code elements

"""
About kwargs: every key should be named like the relative function and has bool value
Example: kwargs = {'general_inspection': True}
The default value is False
"""

import os
from copy import deepcopy


class SureCode:
    def __init__(self, file_name, **kwargs):
        self.file_lines = []
        self.vulnerabilities = {'general_inspection', 'xss', 'sql_injection'}
        self.main(file_name=file_name, **kwargs)

    def main(self, file_name='data/files_to_check/input.py', **kwargs):
        is_file = self.check_file(file_name)
        if not is_file[0]:
            print(is_file[1])  # Errors
            return

        if kwargs.get('general_inspection', False):
            print('general_inspection')
            self.general_inspection(file_name)
        if kwargs.get('xss', False):
            print('xss')
            self.xss(file_name)
        if kwargs.get('sql_injection', False):
            print('sql_injection')
            self.sql_injection(file_name)

    def check_file(self, file_name):
        """
        ru: В переменную self.file_lines заносит список всех строк файла для дальнейшей обработки
        en: Into the self.file_lines variable stores a list of all lines of the file for further processing
        :param file_name:
        :return: True if file is correct, else False
        """
        errors = set()
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                self.file_lines = f.readlines()
            return True,
        else:
            errors.add('Exist')
        return False, errors

    def search(self, what, case=False, new_line=False, begin=None, end=None):
        """ ru: основная функция поиска по алгоритму Р. Боуера и Д. Мура
        en: the main search function using the algorithm of R. Boyer and J. Moore """
        # what = 'print(<all>)'
        # file_name = 'test.py'
        # new_line = True
        # end = ')'

        if case:
            file_lines = deepcopy(self.file_lines)
            what = what.lower()
            for i in range(len(file_lines)):
                file_lines[i] = file_lines[i].lower()
        else:
            file_lines = self.file_lines

        can = False
        res = []
        d = {}
        changeable = []
        what += '~'
        length = len(what)
        for i in range(length - 3, -1, -1):
            d[what[i]] = d.get(what[i], length - i - 2)
        d[what[-1]] = length - 1
        d[what[-2]] = d.get(what[-2], length - 1)
        what = what[:-1]
        elem = what[-1]

        for line, s in enumerate(file_lines):
            la = len(s)
            k = -1
            i = length - 2
            while i < la:
                if s[i] != elem:
                    i += d.get(s[i], d['~'])
                else:
                    if s[i - length + 2:i + 1] == what:
                        k = i - length + 2
                        break
                    i += d[elem]
            if k != -1 and (begin in s or line != 0 and begin in file_lines[line - 1] and
                            (not res or line + 1 not in res[-1])):
                if changeable:
                    res.append(changeable)
                    changeable = []
                if new_line and end not in s:
                    can = True
                changeable.append(line + 1)
            elif can:
                if end in s:
                    changeable.append(line + 1)
                    can = False
                else:
                    changeable.append(line + 1)

        return res

    def general_inspection(self, name):
        """ ru: проверка кода на ненужные элементы
            en: checking the code for unnecessary elements """
        pass

    def xss(self, name):
        """ ru: XSS уязвимость
        en: XSS vulnerability """
        what = 'lol'
        print(self.search(what, name))

    def sql_injection(self, name):
        """ ru: SQLi уязвимость
        en: SQLi vulnerability """
        # can = {
        #     'select': {'new_line': True, 'begin': 'execute(', 'end': ")",
        #                'elements': [['%s'], ['" +', "' +", '""" +', '"+', "'+", '"""+'], ['f"', "f'"]]}
        # }
        can = {
            'select': {'new_line': True, 'begin': 'execute(', 'end': ")",
                       'elements': ['%s', '" +', "' +", '""" +', '"+', "'+", '"""+', 'f"', "f'"]}
        }
        lines_list = self.search(what='select', case=True, new_line=can['select']['new_line'],
                                 begin=can['select']['begin'], end=can['select']['end'])

        res = []
        print(lines_list)
        for lines in lines_list:
            for elem in can['select']['elements']:
                if any([elem in self.file_lines[line - 1] for line in lines]):
                    res.append(lines)
        print(res)


if __name__ == '__main__':
    SureCode('data/files_to_check/xss&sqli.py', general_inspection=False, xss=False, sql_injection=True)
    # SureCode('data/files_to_check/sql.py', general_inspection=False, xss=False, sql_injection=True)
