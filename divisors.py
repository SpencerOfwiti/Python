no = int(input("Enter your Number: "))

listRange = range(2, no + 1)
divisors = []

for i in listRange:
    if no % i == 0:
        divisors.append(i)
    else:
        continue

print(divisors)
