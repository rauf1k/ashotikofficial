password1 = input("Введіть пароль: ")
password2 = input("Знову введіть пароль: ")

if password1 == password2:
    print("Thank you")
elif password1.lower() == password2.lower() or password1.upper() == password2.upper():
    print("They must be in the same case")
else:
    print("Incorrect")