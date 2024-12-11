def personal_sum(numbers):
    result = 0
    incorrect_date = 0
    for i in range(0,len(numbers)):
        try:
            result= result+numbers[i]
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {numbers[i]}')
            incorrect_date +=1
    return [result,incorrect_date]
  
def calculate_average(numbers):
    try:
        count = personal_sum(numbers)
        return  count[0]/(len(numbers)-count[1])
    except ZeroDivisionError as exc:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать


