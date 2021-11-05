revenue = int(input('Write revenue: '))
costs = int(input('Write costs: '))

result = revenue - costs
if result > 0:
    print('Финансовый результат - прибыль')
    profitability = result / revenue
    print((f'Рентабельность - {profitability}'))
    staff = int(input('Write a sum of stuff: '))
    result_staff = result / staff
    print((f'Прибыль на одного сотрудника - {result_staff}'))
else:
    print('Финансовый результат - убыток')
