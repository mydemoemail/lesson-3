# print("Hello")
# умови

# v1
# n1 = 10
# n2 = 20
# v2
# n1, n2 = 10, 20  # множинне привласнення
# print(n1 > n2)
# print(n1 >= n2)
# print(n1 < n2)
# print(n1 <= n2)
# print(n1 == n2)  # поверне True якщо обидва операнди рівні (однакові)
# print(n1 != n2)  # поверне True якщо обидва операнди різні
# #
# print(1 == 1 and 3 == 3)  # поверне True якщо обидва операнди рівні True, інакше False (&&)
# print(1 == 1 or 2 == 3)  # поверне True якщо хоча б один операнд дорівнює True, інакше False (||)
# #
# is_valid = False
# print(is_valid)
# print(not is_valid)  # not -> інверсія, якщо значення False стане True, і навпаки (!is_valid)
#
# print("hello" in "hello world")

##############
# hours = int(input("Enter hours: "))  # int("12")

# v1
# if hours >= 12:
#     print("PM")
# else:
#     print("AM")

# v2
# if 12 <= hours < 24:
#     print("PM")
# elif hours >= 0 and hours < 12:
#     print("AM")
# else:
#     print("Incorrect hours!")

#####
###############
# ввести рейтинг фільму: якщо рейтинг дорівнює 5 або 4 - ок, інакше - погано

# film_rating = int(input("Enter film rating: "))
#
# if 0 < film_rating <= 5:
#     if film_rating == 4 or film_rating == 5:
#         print("OK")
#     else:
#         print("Not ok")
# else:
#     print("Incorrect rating!")

#####################
# 1. create develop branch from master branch
# 2. create feature branch from develop branch

###
# ввести з клавіатури 3 числа
# - вивести найменше із трьох чисел
# - у однакових чисел

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

# вивести найменше із трьох чисел
if number1 < number2 < number3:
    print(number1)
elif number2 < number1 < number3:
    print(number2)
elif number3 < number2 < number1:
    print(number3)
else:
    print("All numbers equals")

