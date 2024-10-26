money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
money_capital=money_capital+salary-spend
count=0
if money_capital>salary:
    count=1
    while money_capital > salary:
        spend=round(spend * (1 + increase),2)
        money_capital=money_capital+salary-spend
        count+=1
print("Количество месяцев, которое можно протянуть без долгов:", count)
