money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
count = 0
duty = 0
while money_capital > duty:
    duty = spend - salary
    money_capital -= duty
    spend *= (1 + increase)
    count += 1
    if money_capital <= duty:
        break

print("Количество месяцев, которое можно протянуть без долгов:", count)
