# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(participants_first_group,participants_second_group,sep_=','):
    list1 = set(list(participants_first_group.split(sep_)))
    list2 = set(list(participants_second_group.split(sep_)))
    result = []

    for x in list2:
        if x in list1:
            result.append(x)
    return result

# TODO Провеьте работу функции с разделителем отличным от запятой
print((find_common_participants(participants_first_group,participants_second_group, sep_=',')))