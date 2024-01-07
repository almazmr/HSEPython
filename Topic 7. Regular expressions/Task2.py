import re

def remove_repeat(string):
    patern = r'\b(\w+)(\s+\1)+\b'
    result = re.sub(patern, r'\1', string)
    return result

some_string = 'Напишите функцию функцию, которая будет будет будет будет \
удалять все все все все последовательные повторы слов из из из из заданной \
строки строки при помощи регулярных выражений'

result = remove_repeat(some_string)
print(result)