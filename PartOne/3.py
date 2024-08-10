a = int(input("Number 1: "))
b = int(input("Number 2: "))

if a >= b:
   start = b
   end = a
else:
   start = a
   end = b
result = 0
while start <= end:
   result += start
   start += 1
print(result)
