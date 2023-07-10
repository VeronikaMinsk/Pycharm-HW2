def decimal_to_hex(decimal):
    hexadecimal_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hexadecimal_digits[remainder] + hexadecimal
        decimal //= 16
    return hexadecimal


number = int(input("Введите целое число: "))
hexadecimal_string = decimal_to_hex(number)
print("Шестнадцатеричное представление числа:", hexadecimal_string)


hex_check = hex(number)[2:].upper()
print("Проверка с использованием функции hex:", hex_check)


if hexadecimal_string == hex_check:
    print("Результат совпадает!")
else:
    print("Результат не совпадает!")
