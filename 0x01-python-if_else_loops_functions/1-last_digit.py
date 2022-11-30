#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
str_1 = str(number)
str_2 = str_1[-1]
int_last_num = int(str_2)

if int_last_num > 5:
    print(f"Last digit of {str_1} is {str_2} and is greater than 5")

elif int_last_num == 0:
    print(f"Last digit of {str_1} is {str_2} and is 0")

elif int_last_num < 6 and int_last_num != 0:
    print(f"Last digit of {str_1} is {str_2} and is less than 6 and not 0")
