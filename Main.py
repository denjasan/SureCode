# encoding: utf-8
# ru: тут основные функции поиска вредоносных элементов кода
# en: here are the main functions for searching for malicious code elements

"""
About kwargs: every key should be named like the relative function and has bool value
Example: kwargs = {'general_inspection': True}
The default value is False
"""

import os


class SureCode:
    def __init__(self, file_name, **kwargs):
        self.file_lines = []
        self.vulnerabilities = {'general_inspection', 'xss', 'sql_injection'}
        print(kwargs)
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

    def search(self, what, file_name):
        """ ru: основная функция поиска по алгоритму Р. Боуера и Д. Мура
        en: the main search function using the algorithm of R. Boyer and J. Moore """
        for line, s in enumerate(open(file_name, 'r').readlines()):
            d = {}
            what += '~'
            length = len(what)
            for i in range(length - 3, -1, -1):
                d[what[i]] = d.get(what[i], length - i - 2)
            d[what[-1]] = length - 1
            d[what[-2]] = d.get(what[-2], length - 1)
            what = what[:-1]
            elem = what[-1]
            i = length - 2
            k = 0
            la = len(s)
            while i < la:
                if s[i] != elem:
                    i += d.get(s[i], d['~'])
                else:
                    if s[i - length + 2:i + 1] == what:
                        k = i - length + 2
                        break
                    i += d[elem]
            if k:
                return line + 1

    def general_inspection(self, name):
        """ ru: проверка кода на ненужные элементы
            en: checking the code for unnecessary elements """
        pass

    def xss(self, name):
        """ ru: XSS уязвимость
        en: XSS vulnerability """
        what = 'mda'
        print(self.search(what, name))

    def sql_injection(self, name):
        """ ru: SQLi уязвимость
        en: SQLi vulnerability """
        pass


if __name__ == '__main__':
    SureCode('data/files_to_check/xss&sqli.py', xss=True, sql_injection=True)
