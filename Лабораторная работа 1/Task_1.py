numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers = [(0 if x is None else x) for x in numbers]
# TODO заменить значение пропущенного элемента средним арифметическим
#numbers[4] = 0
sum_of_numbers = sum(numbers)
len_of_numbers = len(numbers)
average_of_numbers = sum_of_numbers/(len_of_numbers)
numbers = [(average_of_numbers if x is 0 else x) for x in numbers]
#numbers[4] = average_of_numbers
print("Измененный список:", numbers)
