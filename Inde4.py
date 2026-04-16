num = int(input("Enter a number: "))

# Handle negative numbers
num = abs(num)

# Special case for 0
if num == 0:
    count = 1
else:
    count = 0
    while num > 0:
        num = num // 10
        count += 1

print("Number of digits:", count)