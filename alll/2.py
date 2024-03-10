word = input('Введите первые два слова, переданные Александром Поповым:')
words = word.split()
if len(words) == 2 and words[0] == 'Генрих' and words[1] == 'Герц':
    print('Верно!')
else:
    print('Неверно!')
