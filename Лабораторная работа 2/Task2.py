salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
total = spend
for _ in range(2,months + 1):
    spend = spend * (increase + 1)
    total = total + spend

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(total-salary * months))
