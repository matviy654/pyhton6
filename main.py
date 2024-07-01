
# otuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# even_tuple = tuple(x for x in otuple if x % 2 == 0)

# print("Оригінальний кортеж:", otuple)
# print("Кортеж з парними числами:", even_tuple)


# five_element_tuple = (1, 2, 10, 5, 7)
# first1, first2, *middle, last2, last1 = five_element_tuple

# print("Перший елемент:", first1)
# print("Другий елемент:", first2)
# print("Середній елемент (список):", middle)
# print("Передостанній елемент:", last2)
# print("Останній елемент:", last1)

# otuple = (15, 3, 9, 12, 6, 20, 7, 1)


# stuple = tuple(sorted(otuple))

# print("Оригінальний кортеж:", otuple)
# print("Впорядкований кортеж:", stuple)

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# set1 = set(list1)
# set2 = set(list2)
# union_set = set1.union(set2)
# intersection_set = set1.intersection(set2)
# difference_set = set1.difference(set2)
# symmetric_difference_set = set1.symmetric_difference(set2)
# print("Перший список:", list1)
# print("Другий список:", list2)
# print("Об'єднання множин:", union_set)
# print("Перетин множин:", intersection_set)
# print("Різниця множин (set1 - set2):", difference_set)
# print("Симетрична різниця множин:", symmetric_difference_set)

# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (4, 5, 6, 7, 8)
# set1 = set(tuple1)
# set2 = set(tuple2)
# intersection_set = set1.intersection(set2)
# intersection_tuple = tuple(intersection_set)
# print("Перший кортеж:", tuple1)
# print("Другий кортеж:", tuple2)
# print("Спільні елементи (кортеж):", intersection_tuple)


# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (4, 5, 6, 7, 8)


# set1 = set(tuple1)
# set2 = set(tuple2)


# intersection_set = set1.intersection(set2)


# intersection_tuple = tuple(intersection_set)


# print("Перший кортеж:", tuple1)
# print("Другий кортеж:", tuple2)
# print("Спільні елементи (кортеж):", intersection_tuple)

# num_list = [5, 3, 1, 2, 5, 3, 4, 2, 6, 7, 4, 8, 9, 7, 10]


# unique_elements = set(num_list)


# sorted_unique_elements = sorted(unique_elements)


# unique_sorted_tuple = tuple(sorted_unique_elements)


# print("Список чисел:", num_list)
# print("Унікальні елементи:", unique_elements)
# print("Відсортовані унікальні елементи:", sorted_unique_elements)
# print("Кортеж унікальних відсортованих елементів:", unique_sorted_tuple)


# lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]


# sets = [set(lst) for lst in lists]


# union_set = set()
# for s in sets:
#     union_set.update(s)


# print("Список списків:")
# print(lists)
# print("Множини:")
# print(sets)
# print("Об'єднання множин:")
# print(union_set)

# import random

# list_of_tuples = [(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)) for _ in range(10)]

# unique_tuples = set(list_of_tuples)

# print("Список випадкових кортежів:")
# print(list_of_tuples)
# print("Унікальні кортежі:")
# print(unique_tuples)

# numbers = (3, 7, 11, 5, 2)

# total_sum = sum(numbers)

# product = 1
# for num in numbers:
#     product *= num
# average = total_sum / len(numbers)
# print(f"Кортеж чисел: {numbers}")
# print(f"Сума чисел: {total_sum}")
# print(f"Добуток чисел: {product}")
# print(f"Середнє значення чисел: {average}")

# nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))


# element_1 = nested_tuple[0][0]  
# element_2 = nested_tuple[1][1] 
# element_3 = nested_tuple[2][2]  


# print("Елементи з вкладених кортежів:")
# print(element_1)
# print(element_2)
# print(element_3)

# input_list = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 5, 5]

# unique_set = set(input_list)

# max_count = 0
# most_frequent_elements = []

# for element in unique_set:
#     count = input_list.count(element)
#     if count > max_count:
#         max_count = count
#         most_frequent_elements = [element]
#     elif count == max_count:
#         most_frequent_elements.append(element)
# print("Вихідний список з повторюваними елементами:")
# print(input_list)
# print("Унікальні елементи:")
# print(unique_set)
# print("Найчастіше зустрічаються елементи:")
# print(most_frequent_elements)


# list_of_lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

# tuple_of_sets = tuple(set(lst) for lst in list_of_lists)

# print("Список списків:")
# print(list_of_lists)
# print("Кортеж з множин:")
# print(tuple_of_sets)

