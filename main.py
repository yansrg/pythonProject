number1 = int(input("Введіть перше число: "))
number2 = int(input("Введіть друге число: "))
action = input("Виберіть дію: додати(+), відняти(-), помножити(*), поділити(/) --> ")

if action == "+":
    print(number1 + number2)

elif action == "-":
    print(number1 - number2)

elif action == "*":
    print(number1 * number2)

else:
    print(number1 / number2)