def max_dragon_power(total_heads):
    # Если количество голов меньше или равно 7, то самодостаточно возвращаем само число
    if total_heads <= 7:
        return total_heads

    # Начинаем формирование списка, сначала выделяя максимально возможное количество троек
    heads_list = []
    while total_heads >= 3:
        heads_list.append(3)
        total_heads -= 3

    # Если остаток 1, увеличиваем последний элемент списка (переносим голову)
    if total_heads == 1:
        heads_list[-1] += 1
    # Если остаток 2, добавляем его отдельно
    elif total_heads == 2:
        heads_list.append(2)

    # Вычисляем произведение всех голов
    power = 1
    for head in heads_list:
        power *= head

    return power
print(max_dragon_power(12))
