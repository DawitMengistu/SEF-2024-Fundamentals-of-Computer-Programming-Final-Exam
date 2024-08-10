# Write a program that asks the user to input a sentence. If the sentence contains the word "happy,"
#  indicate (print) that it is a positive statement.

words = input("Enter your sentences: ").split()

for i in words:
   if (i == "happy"):
      print("Positive Statment!")
      break
   
# Note that break is not necessary but to stop the loop if we find a single "happy"
