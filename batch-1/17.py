letterCounts = {
    1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6,
    12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6,
    40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 100: 10, 'and': 3, 1000: 8
}

def countLetters(number):
    numLetters = 0
    tensV1 = number // 10
    tensV2 = tensV1 * 10
    units = number % 10
    numLetters += letterCounts[tensV2]
    numLetters += letterCounts[units]
    print(numLetters)

countLetters(42)
