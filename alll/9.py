dog = input('Собака короткошерстной породы?')
if dog == 'да':
    height = input('Рост собаки менее 50 см?')
    if height == 'да':
        tail = input('У собаки короткий хвост?')
        if tail == 'да':
            print('Английский бульдог')
        else:
            ears = input('У собаки длинные уши?')
            if ears == 'да':
                print('Гончая')
            else:
                body = input('У собаки короткое тело?')
                if body == 'да':
                    print('Мопс')
                else:
                    print('Чихуахуа')
    else:
        weight = input('Собака весит более 50 кг?')
        if weight == 'да':
            print('Датский дог')
        else:
            print('Фоксхаунд')
else:
    height_1 = input('Рост собаки менее 50 см?')
    if height_1 == 'да':
        personality = input('У собаки доброжелательный характер? (Да/Нет)')
        if personality.lower() == 'да':
            print('Кокер-спаниэль')
        else:
            print('Ирландский сеттер')
    else:
        height_2 = input('У собаки рост менее 70 см?')
        if height_2 == 'да':
            ears_2 = input('У собаки длинные уши?')
            if ears_2 == 'да':
                print('Большой вандейский грифон')
            else:
                print('Колли')
        else:
            color = input('Окрас рыжий с белыми отметинами?')
            if color == 'да':
                print('Сенбернар')
            else:
                coloring = input('Белоснежный окрас?')
                if coloring == 'да':
                    print('Ирландский волкодав')
                else:
                    print('Ньюфаундленд')

