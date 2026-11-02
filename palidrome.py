num = int(input("Enter a number: "))
original = num
sum = 0

while num > 0:
    r = num % 10
    sum = (sum * 10) + r
    num = int(num/10)
if sum == original:
    print("Your num is an palidrome...", sum)
else:
    print("YOur num is not an palidrome...", sum)