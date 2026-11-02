num = int(input("Enter a number: "))

sum = 0

while num > 0:
    r = num % 10
    sum = sum + r
    num = int(num/10)
print("sum of digit is...", sum)