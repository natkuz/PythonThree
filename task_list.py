# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [1, 2, 2, 3, 3, 4]
all_res = []
for i in my_list:
    if my_list.count(i) > 1:
        all_res.append(i)

res = []
for i in all_res:
    if all_res.count(i) > 1:
        res.append(i)
        all_res.remove(i)
print(res)
