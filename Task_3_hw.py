from fractions import Fraction

fraction1 = input("Введите первую дробь (в формате a/b): ")
fraction2 = input("Введите вторую дробь (в формате a/b): ")

# Разделяем числитель и знаменатель для каждой дроби
numerator1, denominator1 = map(int, fraction1.split('/'))
numerator2, denominator2 = map(int, fraction2.split('/'))

# Создаем объекты Fraction на основе введенных числителей и знаменателей
fraction_obj1 = Fraction(numerator1, denominator1)
fraction_obj2 = Fraction(numerator2, denominator2)

# Вычисляем сумму и произведение дробей
sum_result = fraction_obj1 + fraction_obj2
product_result = fraction_obj1 * fraction_obj2

# Используем модуль fractions для проверки результатов
sum_check = Fraction(fraction1) + Fraction(fraction2)
product_check = Fraction(fraction1) * Fraction(fraction2)

# Выводим результаты и проверку
print("Сумма дробей:", sum_result)
print("Произведение дробей:", product_result)
print("Проверка суммы с помощью модуля fractions:", sum_result == sum_check)
print("Проверка произведения с помощью модуля fractions:", product_result == product_check)