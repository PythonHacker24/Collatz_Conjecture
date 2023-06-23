# This program represents the Collatz Conjecture

import time
import matplotlib.pyplot as plt
from matplotlib import style

def check(num):
	if num % 2 == 0:
		return 1
	else:
		return 0

def loop_detector(history_array, check_num, history_depth, counter):
	if counter <= history_depth:
		init_pointer = 0
	if counter > history_depth:
		init_pointer = counter - history_depth

	for i in range(init_pointer, counter):
		if check_num == history_array[i]:
			return 1
		else:
			return 0
	
def collatz_conjecture(num):
	if check(num) == 1:
		num = num / 2
	elif check(num) == 0:
		num = 3*num + 1
	return num

def operation(num, interval, history_depth):
	counter = 0
	history_array = [num]
	counter_timer = [0]
	while True:
		loop = loop_detector(history_array, num, history_depth, counter)
		
		num = collatz_conjecture(num)
		history_array.append(num)
		print(history_array[counter + 1])

		# Temporary loop detector for 4, 2, 1 pattern
		if num == 1:
				print("Loop detected! .... 4, 2, 1")
				#exit()
				counter += 1
				counter_timer.append(counter)

				return history_array, counter_timer

		if loop == 1:
			print("[+] Loop detected! .... ")
			break
		else:
			pass
		counter_timer.append(counter)
		counter += 1
		time.sleep(interval)
	
num = int(input("Enter the initial number: "))
interval = float(input("Enter the interval to between computations: "))

history_depth = 50
outcome_array, counter_timer = operation(num, interval, history_depth)

outcome_sum = 0
for i in range(len(outcome_array)):
	outcome_sum += outcome_array[i]

outcome_average = outcome_sum/len(outcome_array)
print("Average of every outcome value: " + str(outcome_average))

# average_list = []
# for i in range(len(counter_timer)):
# 	average_list.append(outcome_average)

sum_first_digit = 0
for num in outcome_array:
	first_digit = int(str(num)[0])
	sum_first_digit += first_digit
	print(first_digit)
print("Average of first digits: " + str(sum_first_digit/len(outcome_array)))



# Uncomment to plot the Graph
# print("Average: " + str(average))

# style.use('dark_background')
# plt.plot(counter_timer, history_array)
# plt.plot(counter_timer, average_list)

# plt.xlabel('Steps')
# plt.ylabel('Value at each Step')
# plt.title('The Collatz Conjecture')

# plt.show()

""" 

Notes

1. Work upon the loop detector. The array index goes out of range due to algorithm failure.
2. Graph ploting works! It's time to implement advance loop detection algorithm
3. The history_array is working, work upon the loop detection algorithm.

"""
