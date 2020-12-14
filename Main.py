# encoding: utf-8
# ru: тут основные функции поиска вредоносных элементов кода
# en: here are the main functions for searching for malicious code elements


def search(what, file_name):
    """ ru: основная функция поиска по алгоритму Р. Боуера и Д. Мура
    en: the main search function using the algorithm of R. Boyer and J. Moore """
    with open(file_name, 'r') as file:
        for line_number, line in enumerate(file.readlines()):
            pass


def xxs():
    """ ru: XXS уязвимость
    en: XXS vulnerability """
    pass


def sql_injection():
    """ ru: SQLi уязвимость
    en: SQLi vulnerability """
    pass




