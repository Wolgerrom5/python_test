def can_gears_rotate(num_gears, gear_teeth):
    total = sum(gear_teeth)
    if total == 0:
        return True
    else:
        return False

# Пример использования программы
num_gears = int(input("Введите количество шестеренок: "))
gear_teeth = []

for i in range(2):
    teeth = int(input(f"Введите количество зубьев для шестеренки {i+1}: "))
    gear_teeth.append(teeth)

if can_gears_rotate(num_gears, gear_teeth):
    print("Шестерёнки могут вращаться")
else:
    print("Шестерёнки не могут вращаться")