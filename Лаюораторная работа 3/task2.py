# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, sep=','):
    first=set(first.split(sep))
    second=set(second.split(sep))
    common=list(first.intersection(second))
    common.sort()
    return(common)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
sep='|'
print(find_common_participants(participants_first_group,participants_second_group,sep))

# TODO Провеьте работу функции с разделителем отличным от запятой
participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

print(find_common_participants(participants_first_group,participants_second_group))

