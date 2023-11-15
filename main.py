import numpy as np

def ListToNumpy(arr):
    return np.array(arr, dtype=float)

def ShapeSizeCalc(arr):
    shape = arr.shape
    size = arr.size
    return shape, size

def ShapeSizeCalc(arr):
    shape = arr.shape
    size = arr.size
    return shape, size

arr = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])

result_shape, result_size = ShapeSizeCalc(arr)
print("Shape:", result_shape)
print("Size:", result_size)

rows = (0, 1)
selected_rows = arr[rows, :]
print("Selected Rows:")
print(selected_rows)

val = 2
indices = np.where(arr == val)
print(f"Indices of {val}:", indices)



import calendar

print(calendar.isleap(2027))

weekday_1995_06_25 = calendar.weekday(1995, 6, 25)
print(weekday_1995_06_25)

cal_2023 = calendar.TextCalendar().formatyear(2023)
print(cal_2023)

from fuzzywuzzy import fuzz, process

print(dir(fuzz))
   
similarity_ratio = fuzz.ratio('Плохой код на самом деле не плохой.', 'Его просто не так поняли.')
print(f"Схожесть: {similarity_ratio}%")
   
similarity_ratio_2 = fuzz.ratio('Работает? Не трогай.', 'Работает? Не трогай.')
print(f"Схожесть: {similarity_ratio_2}%")

similarity_ratio_3 = fuzz.ratio('Работает? Не трогай.', 'Работает? Не трогай!')
print(f"Схожесть: {similarity_ratio_3}%")
   

