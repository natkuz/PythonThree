# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

capacity = 10
things = {'топор': 2,
          'вода': 1,
          'спички': 0.2,
          'палатка': 2,
          'еда': 1.5,
          'дрова': 3,
          'средство от комаров': 0.2,
          'рыболовные снасти': 1.5,
          'мяч': 0.3,
          'бадминтон': 0.2}

wheight = 0
get_things = []

for key, value in things.items():
        wheight = wheight + value
        if wheight <= capacity:
            get_things.append(key)
        else:
            break
print(f'В рюкзак поместятся: {", ".join([i for i in get_things])}')