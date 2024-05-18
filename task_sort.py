from timeit import timeit
import random
import matplotlib.pyplot as plt

# Ідея коду:
#   Набрати статистику часу, за який виконується кожне сортування. Зобразити розподіл результатів на одному графіку. Зробити висновки.
#   
# Реалізація:
#   1. Напишемо функцію, яка випадково генерує набір цілочислених масивів бажаного розміру в бажаній кількості.
#   2. Замірятимемо час сортування кожного з отриманих масивів для трьох заданих алгоритмів сортування.
#   3. Зобразимо графічно результати вимірювань.
#   4. Повторимо процес для наборів масивів різних розмірів.

def generate_list_of_arrays(number, length): 
    """
    Функція для генерації NUMBER цілочисельних масивів довжиною LENGTH
    """
    
    # Initialize the list to hold all arrays
    arrays_list = []

    # Generate the arrays
    for _ in range(number):
        array = [random.randint(0, 10000) for _ in range(length)]
        arrays_list.append(array)
    
    return arrays_list

# СОРТУВАННЯ ЗЛИТТЯМ (взято з конспекту)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# СОРТУВАННЯ ВСТАВКАМИ (взято з конспекту)
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def time_results(list_of_arrays):
    """
    Функція отримує на вхід набір цілочисельних масивів, а далі проводить вимірювання часу, за який кожен масив відсортується кожним з трьох заданих алгоритмів сортування.
    Повертає три масиви: результати першого алгоритму сортування, другого і третього.
    """

    time_results_merge = []
    time_results_insertion = []
    time_results_standart = []

    # Набираємо статистику тривалості різних сортувань
    for array in list_of_arrays:
        time_results_merge.append(timeit(f'{merge_sort(array)}', number=100))
        time_results_insertion.append(timeit(f'{insertion_sort(array)}', number=100))
        time_results_standart.append(timeit(f'{array.sort()}', number=100))             #  <--  Результат залежить від того, як ми напишемо: f'{array}.sort()' або f'{array.sort()}'
                                                                                        #       В першому випадку сортування TimSort завжди дає найповільніший результат.
                                                                                        #       В другому - TimSort швидший.
    return time_results_merge, time_results_insertion, time_results_standart

def draw_histograms(arrays, bins=20):
    """
    Draw histograms for a list of integer arrays in a single window.

    Parameters:
        arrays (list of lists): List of integer arrays.
        bins (int): Number of bins for the histograms.
    """
    
    plt.figure()
    
    for array, color, label in zip(arrays, ['blue', 'red', 'green'], ['merge', 'insertion', 'standart']):
        plt.hist(array, bins=bins, color=color, label=label, histtype='bar')
        plt.legend()
 
draw_histograms(time_results(generate_list_of_arrays(1000, 10)))
draw_histograms(time_results(generate_list_of_arrays(1000, 100)))
draw_histograms(time_results(generate_list_of_arrays(1000, 1000)))

plt.show()

# Промальовка невдала, але не знаю поки як пофіксити.
# 
# Спочатку "рахується" кожна окрема гістограма, тим самим визначаючи власну ширину стовпчиків 
# (інтервал, в якому лежить гістограма, поділений на кількість стовпчиків bins=20)
# 
# TimSort займає меньший інтервал по часу, тому й стовпчики виходять вужчими.
# 
# Щоб побачити зелену гістограму розподілу TimSort, треба вбудованим інструментом збільшення картинки збільшити все що лівіше червоної та синьої гістограм.