initial_amount = 0
current_amount = initial_amount
transaction_count = 0
tax_rate = 0.1
transaction_limit = 5000000

while True:
    print("Сумма денег:", current_amount)
    action = input("Выберите действие (пополнить, снять, выйти): ")

    if action == "выйти":
        print("Программа завершена.")
        break

    elif action == "пополнить":
        amount = int(input("Введите сумму пополнения: "))
        if amount % 50 != 0:
            print("Сумма пополнения должна быть кратной 50 у.е.")
            continue

        current_amount += amount
        transaction_count += 1

        if transaction_count % 3 == 0:
            current_amount *= 1.03

    elif action == "снять":
        amount = int(input("Введите сумму снятия: "))
        if amount % 50 != 0:
            print("Сумма снятия должна быть кратной 50 у.е.")
            continue

        if amount > current_amount:
            print("Недостаточно средств на счете.")
            continue

        if current_amount > transaction_limit:
            current_amount -= current_amount * tax_rate

        commission = amount * 0.015
        commission = max(commission, 30)
        commission = min(commission, 600)

        current_amount -= amount + commission
        transaction_count += 1

    else:
        print("Некорректное действие. Попробуйте снова.")
        continue
