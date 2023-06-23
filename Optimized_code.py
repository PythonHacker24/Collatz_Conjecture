import time
import matplotlib.pyplot as plt

def collatz_conjecture(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

def operation(num, interval, history_depth):
    history_set = set([num])
    history_list = [num]
    counter_timer = [0]
    counter = 0

    while True:
        num = collatz_conjecture(num)
        history_list.append(num)

        if num == 1:
            print("Loop detected! .... 4, 2, 1")
            counter += 1
            counter_timer.append(counter)
            return history_list, counter_timer

        if num in history_set:
            print("[+] Loop detected! .... ")
            break

        counter_timer.append(counter)
        counter += 1
        time.sleep(interval)

    return history_list, counter_timer

num = int(input("Enter the initial number: "))
interval = float(input("Enter the interval between computations: "))
history_depth = 50

outcome_array, counter_timer = operation(num, interval, history_depth)

outcome_sum = sum(outcome_array)
outcome_average = outcome_sum / len(outcome_array)
print("Average of every outcome value:", outcome_average)

sum_first_digit = sum(int(str(num)[0]) for num in outcome_array)
average_first_digit = sum_first_digit / len(outcome_array)
print("Average of first digits:", average_first_digit)

