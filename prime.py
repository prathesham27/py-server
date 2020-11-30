num = int(input("Enter The Number:"))
for i in range(2, num):
    if num % 2 == 0:
        print(num, "is not a Prime Number")
        break
else:
    print(num, "is a Prime")