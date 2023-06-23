import time
import matplotlib.pyplot as plt
from matplotlib import style

def check(num):
    if num % 2 == 0:
        return 1
    else:
        return 0

def collatz_conjecture(num):
    if check(num) == 1:
        num = num / 2
    elif check(num) == 0:
        num = 3*num + 1
    return num

def operation(num, interval):
    counter = 0
    history_array = [num]
    counter_timer = [0]
    while True:
        num = collatz_conjecture(num)
        history_array.append(num)
        if num == 1:
            counter += 1
            counter_timer.append(counter)
            return history_array, counter_timer
        counter_timer.append(counter)
        counter += 1
        time.sleep(interval)

average_values_first_digit = []
average_values_outcomes = []

compute_value = 10000000
for num in range(1, compute_value):
    interval = 0
    outcome_array, counter_timer = operation(num, interval)

    outcome_sum = 0
    for i in range(len(outcome_array)):
        outcome_sum += outcome_array[i]

    outcome_average = outcome_sum / len(outcome_array)
    average_values_outcomes.append(outcome_average)

    counter = 0
    for num in outcome_array:
        first_digit = int(str(num)[0])
        counter += first_digit

    average_values_first_digit.append(counter / len(outcome_array))

style.use('dark_background')
plt.plot([i for i in range(1, compute_value)], average_values_outcomes)
plt.show()
