class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self,message):
        self.message = message

class Car:
    def __init__(self,model,vin_number,numbers):
        self.model = model
        if self.__is_valid_vin(vin_number):
            self.__vin = vin_number
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self,vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        elif not (vin_number >= 1000000 and vin_number <= 9999999):
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        else:
            return True
    def __is_valid_numbers(self,numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        elif len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        else:
            return True

def New_Car(model,vin,number):
    try:
        car_ = Car(model,vin,number)
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{car_.model} успешно создан')
        return car_

first = New_Car('Model1', 1000000, 'f123dj')
second = New_Car('Model2', 300, 'т001тр')
third = New_Car('Model3', 2020202, 'нет номера')
