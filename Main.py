# encoding: utf-8
# ru: тут основные функции поиска вредоносных элементов кода
# en: here are the main functions for searching for malicious code elements

import os


class SureCode:
    def __init__(self, file_name, xss_on, sqli_on):
        self.file_lines = []
        self.main(file_name=file_name, xss_on=xss_on, sqli_on=sqli_on)

    def main(self, file_name='data/files_to_check/input.py', xss_on=True, sqli_on=True):
        if not self.check_file(file_name):
            return
        if xss_on:
            pass
        if sqli_on:
            pass

    def check_file(self, file_name):
        """
        ru: В переменную self.file_lines заносит список всех строк файла для дальнейшей обработки
        en: Into the self.file_lines variable stores a list of all lines of the file for further processing
        :param file_name:
        :return: True if file is correct, else False
        """
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                self.file_lines = f.readlines()
            return True
        return False

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
    SureCode(file_name='data/files_to_check/xss&sqli.py')




