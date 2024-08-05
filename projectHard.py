grades = [[5, 3, 4, 5, 4], [2, 5, 2, 3], [4, 3, 5, 3], [4, 4, 5], [3, 3, 4, 4, 5]]
students = {'Кирилл', 'Михаил', 'Оксана', 'Елена', 'Антон'}

# для начала расчитаем среднее значение оценок в списке будем использовать функцию sum  для сложения и делить
# на колличество символов в списке, для этого пишем функцию len

grades_list = [(sum(grades[0]) / len(grades[0])),(sum(grades[1]) / len(grades[1])),(sum(grades[2]) / len(
grades[2])),(sum(grades[3]) / len(grades[3])),(sum(grades[4]) / len(grades[4]))]

print(grades_list)

#далее отсортируем имена в алфавитном порядке и множество приведем к списку
students_list = sorted(list(students))

print(students_list)
# теперь создаем словарь в котором ключ - Имя ученика, а значение - средний балл

grades_dict = dict(zip(students_list, grades_list))

print(grades_dict)