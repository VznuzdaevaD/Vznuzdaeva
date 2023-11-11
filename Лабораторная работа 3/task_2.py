# TODO Напишите функцию find_common_participants

def find_common_participants(str_1, str_2, separator = ","):
    separated_1 = str_1.split(separator)
    separated_2 = str_2.split(separator)
    answer = list(set(separated_1).intersection(separated_2))
    answer.sort()
    return answer

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_first_group, separator = ","))
# TODO Провеьте работу функции с разделителем отличным от запятой
