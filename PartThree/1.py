# Write a program that calculates and prints the sum of the digits of a given positive integer. The program should work for integers of any length.


numbers = input("Enter a number: ")
sum = 0

for i in numbers:
    sum += int(i)

print(sum)
