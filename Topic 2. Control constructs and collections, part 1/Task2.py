'''
Задание 2 (необязательное)
Написать код на Python в среде Jupyter Notebook для решения следующей задачи.

Вы делаете MVP (минимально жизнеспособный продукт) dating-сервиса.
У вас есть список юношей и девушек.
Выдвигаем гипотезу: лучшие рекомендации получатся, если просто отсортировать имена по алфавиту и познакомить людей с одинаковыми индексами после сортировки. Но вы не будете никого знакомить, если кто-то может остаться без пары.

Примеры работы программы:

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard'] 
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'] 

Результат:
Идеальные пары:
Alex и Emma
Arthur и Kate
John и Kira
Peter и Liza
Richard и Trisha

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael'] 
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'] 

Результат: Внимание, кто-то может остаться без пары!
'''

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma']
sorted_boys = sorted(boys)
sorted_girls = sorted(girls)

print("Идеальные пары:")
for boy, girl in zip(sorted_boys, sorted_girls):
    print(boy, "и", girl)

if len(boys) > len(girls):
    print("Остался без пары:", boys[-1])
elif len(girls) > len(boys):
    print("Осталась без пары:", girls[-1])