
tvshow = ["Зваженні та щастливі", "Орел і Решка", "Вагітна у 16", "Хочу залік"]

print("Список телешоу:")
for item in tvshow:
    print(item)


new_value = input("Введіть телешоу яке хочете внести в список: ")
position = int(input("Введіть позицію на якій буде телешоу (0-4): "))


tvshow.insert(position, new_value)

print("Новий список:")
for item in tvshow:
    print(item)