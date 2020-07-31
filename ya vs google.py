from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

search_system = [{'name': 'google'}, {'name': 'yandex'}]


def input_link():
    link = input('enter test link between search system ')
    link.find('.')
    return link


def choise_search_system():
    global search_system
    print('select two search engines and enter through a space')
    flag1, flag2 = True, True
    while flag1 or flag2:
        for i in search_system:
            print(i['name'], end=' ')
        try:
            sys1, sys2 = [str(x) for x in input().split()]
            if sys1 == sys2:
                print('вы ввели одну и туже поисковую систему')
            else:
                for i in search_system:
                    if sys1 == i['name']:
                        flag1 = False
                    if sys2 == i['name']:
                        flag2 = False
            if (sys1 != sys2) and (flag1 or flag2):
                print('вы ввели несушествующую поисковую систему')
        except ValueError:
            print('Нужно вводить через пробел')
    return sys1, sys2



class Yandex:
    pass


class Google:
    pass


def main():
    for i in range(5):
        choise_search_system()


if __name__ == '__main__':
    print(input_link())