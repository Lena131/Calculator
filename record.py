def log(separate_expression, result):
    expression = ' '.join(map(str, separate_expression))
    with open('expression.txt', 'a') as data:
        data.write(f'{expression} = {result}\n')