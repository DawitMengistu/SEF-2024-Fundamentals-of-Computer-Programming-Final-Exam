# Write a program that asks the user to enter two numbers, swap their values  and print them.

num_one = 4
num_two = 9

temp = num_one # temporary varibale to store num_one
num_one = num_two
num_two = temp

print(num_one, num_two)