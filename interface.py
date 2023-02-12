
from calculation import parse, calculate
from result import view_result as view
from record import log

def button_click():
    flag = input('Введите ' 'пробел-Enter, чтобы продолжить, или Enter, чтобы прервать работу программы ')
    while flag == ' ':
        separate_expression = parse()
        result = calculate(separate_expression)
        log(separate_expression, result)
        view(result)
        flag = input('Введите ' 'пробел-Enter, чтобы продолжить, или Enter, чтобы прервать работу программы ')
    print('Программа завершена.')