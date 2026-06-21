# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
ML_LITER = 1000


print("Добро пожаловать в фитнес-трекер от FitLife")

# 1. Знакомство
while True:
    user_name = input("Введите имя: ").strip()
    if user_name != "":
        user_name = user_name.title()
        break
    print("Имя не может быть пустым или пробелом!")
while True:
    user_age = input("Введите возраст: ").strip()
    try:
        user_age_int = int(user_age)
        if user_age_int > 0:
            break
        print("Возраст должен быть больше нуля!")
    except ValueError:
        print("Укажите возраст в цифрах!")
# 2. Сбор данных
while True:
    user_weight = input("Введите вес в кг (пример, 75): ").strip()
    try:
        user_weight_float = float(user_weight)
        if user_weight_float > 0:
            break
        print("Вес должен быть больше нуля!")
    except ValueError:
        print("Укажите вес в цифрах (например, 75)")
while True:
    user_height = input("Введите рост в м (c точкой,например 1.75): ").strip()
    try:
        user_height_float = float(user_height)
        if user_height_float > 0:
            break
        print("Рост должен быть больше нуля!")
    except ValueError:
        print("Укажите рост в цифрах (используя точку,например 1.75)")
# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# расчёт индекса массы тела
bmi = user_weight_float / (user_height_float ** 2)
bmi = round(bmi, 1)
# расчет нормы воды
water_ml = user_weight_float * WATER_PER_KG
water_l = water_ml / ML_LITER

# 4. Вывод красивого результата
print(f"Отчет для пользователя: {user_name} ({user_age_int} г.)")
print(f"Твой Индекс Массы Тела: {bmi}")
if bmi < 18.5:
    print("Дефицит массы тела")
elif bmi < 25.0:
    print("Нормальный вес")
elif bmi < 30.0:
    print("Избыточный вес")
else:
    print("Ожирение")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
