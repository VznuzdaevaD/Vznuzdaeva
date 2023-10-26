numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index_missing_number = 4

sum_ = sum(numbers[:index_missing_number]) + sum(numbers[index_missing_number+1:])
len_ = len(numbers)

numbers[4] = sum_/len_

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
