# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(participants_first_group,participants_second_group,sep_=','):
    set1_ = set(list(participants_first_group.split(sep_)))
    set2_ = set(list(participants_second_group.split(sep_)))
    result = []

    for x in set2_:
        if x in set1_:
            result.append(x)
    return result
    print(list(result).sort())
print((find_common_participants(participants_first_group,participants_second_group,sep_=',')))


# TODO Провеьте работу функции с разделителем отличным от запятой
