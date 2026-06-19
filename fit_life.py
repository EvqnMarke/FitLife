# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
ML_LITER = 1000


print("Добро пожаловать в фитнес-трекер от FitLife")

# 1. Знакомство
user_name = input("Введите имя: ")
user_name = user_name.title()
user_age = input("Введите возраст: ")
user_age_int = int(user_age)

# 2. Сбор данных
user_weight = input("Введите вес в кг (например, 75): ")
user_weight_float = float(user_weight)
user_height = input("Введите рост в м (используя точку,например 1.75): ")
user_height_float = float(user_height)

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
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
