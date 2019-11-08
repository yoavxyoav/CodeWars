# https://www.codewars.com/kata/59590976838112bfea0000fa/train/python

def beggars(values, n):
    result = []
    for i in range(n):
        accumulator = 0
        for j in range(i, len(values), n):
            accumulator += values[j]
        result.append(accumulator)
    return result
