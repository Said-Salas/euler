letterCounts = {
    1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6,
    12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6,
    40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 10, 1000: 8
}

def countLetters(number):
    numLetters = 0
    if number in letterCounts:
        numLetters = letterCounts[number]
    else:
        numDigits = 0

        for i in str(number):
            numDigits += 1
        print(f"Number of digits is {numDigits}")   

        while numDigits > 1:
            if numDigits > 2:
                numList = list(str(number))
                print(f"The number as a list is: {numList}")
                part = int((numList[0])) * 100
                print(f"The first part is {part}")
                print(f"Which corresponds to a value of {letterCounts[part]}")
                numLetters += letterCounts[part] + 3
                numList.pop(0)
                number = int("".join(map(str, numList)))

            part = (number // 10) * 10
            numLetters += letterCounts[part]
            numDigits -= 1
        
        units = number % 10
        numLetters += letterCounts[units]

    print(numLetters)

countLetters(194)
