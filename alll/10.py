def number_of_gears(n):
    if n % 2 == 0:
        return "Шестеренки могут вращаться"
    else:
        return "Шестеренки не могут вращаться"

n = int(input("Введите количество шестеренок в последовательности: "))
print(number_of_gears(n))