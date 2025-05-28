def sum_to_n(n, accumulator=0):
    if n <= 0:
        return accumulator
    return sum_to_n(n - 1, accumulator + n)