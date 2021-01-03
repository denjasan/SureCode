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

        what_to_do = self.kwargs_transformation(**kwargs)
        print(what_to_do)
        if what_to_do.get('general_inspection', False):
            print('general_inspection')
        if what_to_do.get('xss', False):
            print('xss')
        if what_to_do.get('sql_injection', False):
            print('sql_injection')

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
            return True, None
        else:
            errors.add('Exist')
        return False, errors

    def kwargs_transformation(self, **kwargs):
        new_dict = {}
        for key, value in kwargs.items():
            print(key == "xss")
            # if key in self.vulnerabilities:
            #     new_dict[key] = kwargs.get(key, False)
        return new_dict

    def search(self, what, file_name):
        """ ru: основная функция поиска по алгоритму Р. Боуера и Д. Мура
        en: the main search function using the algorithm of R. Boyer and J. Moore """
        for line_number, line in enumerate(self.file_lines):
            pass

    def general_inspection(self):
        """ ru: проверка кода на ненужные элементы
            en: checking the code for unnecessary elements """
        pass

    def xxs(self, name):
        """ ru: XXS уязвимость
        en: XXS vulnerability """
        pass

    def sql_injection(self, name):
        """ ru: SQLi уязвимость
        en: SQLi vulnerability """
        pass


if __name__ == '__main__':
    SureCode('data/files_to_check/xss&sqli.py', xxs=True, sql_ingection=True)
