numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
right_numbers=numbers[5:]
left_numbers=numbers[:4]
count_numbers=len(numbers)
sum_numbers=sum(left_numbers+right_numbers)
average= sum_numbers/count_numbers
numbers[4]=average

print("Измененный список:", numbers)
