base = 2

for i in range(1, 21):
    num = base ** i
    sumA = 0
    digits = [int(digit) for digit in str(num)]
    for digit in digits:
        sumA += digit
    print(num, sumA)