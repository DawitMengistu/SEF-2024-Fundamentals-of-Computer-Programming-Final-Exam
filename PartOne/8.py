i = 1
while i < 10:
    if i%2 == 0:
        i = i+1
        continue
    if i == 7:
        break
    print(i)
    i = i+1

