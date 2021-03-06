# encoding: utf-8
# ru: тут основные функции поиска вредоносных элементов кода
# en: here are the main functions for searching for malicious code elements

"""
About kwargs: every key should be named like the relative function and has bool value
Example: kwargs = {'xss': True}
The default value is False
"""

import os
from copy import deepcopy

description = {'render_template_string': "Use render_template() instead of render_template_string()",
               'render_template': "Only use .html extensions for templates",
               'Template': "Use render_template()",
               '.Template': "Use render_template()",
               'arkup(': "Don't use Markup():",
               'django': "Use django.utils.html.format_html",
               'autoescape false': "Don't disable the autoescape system in templates",
               'safe': "Don't mark a string as safe HTML",
               'sql_injection': "Use '?' when adding variables to an SQL query. For example:\
            \ncur.execute('SELECT id, username FROM `user` WHERE username = ? AND password = ?', (username, password))"}


class SureCode:
    def __init__(self, file_name, **kwargs):
        self.file_lines = []
        self.vulnerabilities = {'xss': {}, 'sql_injection': {}}
        self.main(file_name=file_name, **kwargs)

    def main(self, file_name='data/files_to_check/xss&sqli.py', **kwargs):
        is_file = self.check_file(file_name)
        if not is_file[0]:
            print(is_file[1])  # Errors
            return

        if kwargs.get('xss', False):
            self.vulnerabilities['xss'] = self.xss()
        if kwargs.get('sql_injection', False):
            self.vulnerabilities['sql_injection'] = self.sql_injection()

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
            errors.add("File doesn't exist in the specified directory")
        return False, errors

    def search(self, what, case=False, new_line=False, begin=None, end=None):
        """
        ru: основная функция поиска по алгоритму Р. Боуера и Д. Мура
        en: the main search function using the algorithm of R. Boyer and J. Moore
        :return: Список списков, содержащий строки вхождения нужного элемента
        """

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
        if changeable:
            res.append(changeable)
        return res

    def xss(self):
        """ ru: XSS уязвимость
        en: XSS vulnerability """
        can = {
            'render_template_string': {'new_line': True, 'begin': 'return ', 'end': ")"},
            'render_template': {'new_line': True, 'begin': 'return ', 'end': ")",
                                'elements': ['.htm)', '.xml', '.xhtml', '.jinja2']},
            'Template': {'new_line': True, 'begin': 'from', 'end': ""},
            '.Template': {'new_line': True, 'begin': 'jinja2', 'end': ""},
            'arkup(': {'new_line': True, 'begin': 'M', 'end': ")"},
            'django': {'new_line': False, 'begin': 'import ', 'end': "\n"},
            'autoescape false': {'new_line': True, 'begin': '{%', 'end': "endautoescape "},
            'safe': {'new_line': False, 'begin': '|', 'end': "}"},
        }
        res = []
        result = {}
        need_elem = {'render_template'}
        for what in can.keys():
            lines_list = self.search(what=what, case=False, new_line=can[what]['new_line'],
                                     begin=can[what]['begin'], end=can[what]['end'])
            if lines_list:
                if what in need_elem:
                    for lines in lines_list:
                        for elem in can[what]['elements']:
                            if any([elem in self.file_lines[line - 1] for line in lines]):
                                res.append(lines)
                if res:
                    result[what] = res
                    res = []
                elif what not in need_elem:
                    result[what] = lines_list
        return result

    def sql_injection(self):
        """ ru: SQLi уязвимость
        en: SQLi vulnerability """
        can = {
            'select': {'new_line': True, 'begin': 'execute(', 'end': ")", 'case': True},
            'delete': {'new_line': True, 'begin': 'execute(', 'end': ")", 'case': True},
            'insert': {'new_line': True, 'begin': 'execute(', 'end': ")", 'case': True}
        }

        elements = ['%s', '" +', "' +", '""" +', '"+', "'+", '"""+', 'f"', "f'"]
        res = []
        for what in can.keys():
            lines_list = self.search(what=what, case=can[what]['case'], new_line=can[what]['new_line'],
                                     begin=can[what]['begin'], end=can[what]['end'])
            for lines in lines_list:
                for elem in elements:
                    if any([elem in self.file_lines[line - 1] for line in lines]):
                        res.append(lines)
        return {'sql_injection': res}


if __name__ == '__main__':
    ob = SureCode('data/files_to_check/input.py', general_inspection=False, xss=True, sql_injection=True)
    print('')
    for vulnerability in ob.vulnerabilities.keys():
        print(vulnerability, ':', sep='')
        for j in ob.vulnerabilities[vulnerability].keys():
            print(j, ob.vulnerabilities[vulnerability][j])
            print('Description:', description[j])
            print('____________')
        print('__________________________________________________________')
