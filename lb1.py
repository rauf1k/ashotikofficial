hochuzachetik = [
  [2, 5, 8],
  [3, 7, 4],
  [1, 6, 9],
  [4, 2, 0]
]

stolb = int(input("Введіть номер стовпця від 0 до 3:"))
ryadok = int(input("Введіть номер рядка від 0 до 2:"))

number = hochuzachetik[stolb][ryadok]

print(f"Номер в стовпці {stolb} в рядку {ryadok} це {number}")
