# This program represents the Collatz Conjecture

import time
import matplotlib.pyplot as plt
from matplotlib import style
from numba import jit, cuda
import timeit

start = timeit.default_timer()

def check(num):
	if num % 2 == 0:
		return 1
	else:
		return 0

# @jit(target_backend='cuda')
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
		#print(history_array[counter + 1])
		if num == 1:
				#print("Loop detected! .... 4, 2, 1")
				counter += 1
				counter_timer.append(counter)
				return history_array, counter_timer
		counter_timer.append(counter)
		counter += 1
		time.sleep(interval)
	
average_values_first_digit = []
average_values_outcomes = []


compute_value = int(input("[+] Enter the interval range from 1 to n [1, n]: "))
for num in range(1,compute_value):
	print("[+] Computing for: " + str(num) + "    Progress: " + str(num/compute_value * 100) + "%", end="\r")
	#print("---------------- Computing " + str(num) + " --------------------")
	interval = 0
	outcome_array, counter_timer = operation(num, interval)

	outcome_sum = 0
	for i in range(len(outcome_array)):
		outcome_sum += outcome_array[i]

	outcome_average = outcome_sum/len(outcome_array)
	#print("Average of every outcome value: " + str(outcome_average))
	average_values_outcomes.append(outcome_average)

	counter = 0
	for num in outcome_array:
		first_digit = int(str(num)[0])
		counter += first_digit

	style.use('dark_background')
	plt.plot([i for i in range(len(outcome_array))], outcome_array)
	#print("Average of first digits: " + str(counter/len(outcome_array)))
	average_values_first_digit.append(counter/len(outcome_array))

stop = timeit.default_timer()

print("[+] Runtime of the Program:" + str(stop - start))  

binaryhash = ""
for i in average_values_outcomes:
	binaryhash = binaryhash + str(bin(int(i)).replace("0b", ""))

hash_file = open("hash", "w")
hash_file.write(binaryhash)
hash_file.close()

print("[+] Length of hash: " + str(len(binaryhash)))

one  = 0
zero = 0

for i in binaryhash:
	if i == str(0):
		zero += 1
	elif i == str(1):
		one += 1

one_prob = one / (one + zero)
print("[+] Probability for occurance of 1 in binary hash: " + str(one_prob))

# style.use('dark_background')
# plt.plot([i for i in range(1,compute_value)], average_values_outcomes)
plt.show()

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
4. Work on seperating the computational and storage part to make the computational part run on GPU 
5. Optmise the code to run on the GPU

"""
