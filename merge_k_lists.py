import random

def generate_sorted_list(length):
    sorted_list = []
    last_element = 0
    for _ in range(length):
        last_element += random.randint(0, 50)
        sorted_list.append(last_element)
    return sorted_list


# СОРТУВАННЯ ЗЛИТТЯМ (взято з конспекту)
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]

#     return merge(merge_sort(left_half), merge_sort(right_half))

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



def merge_k_lists(sorted_lists):
    if len(sorted_lists) == 1:
        return sorted_lists[0]
    elif len(sorted_lists) == 2:
        return merge(sorted_lists[0], sorted_lists[1])
    else:
        return merge(sorted_lists[0], merge_k_lists(sorted_lists[1:]))


sorted_lists = []

for i in range(1, 11, 2):
    sorted_lists.append(generate_sorted_list(i))
    
merged = merge_k_lists(sorted_lists)
print(merged)
