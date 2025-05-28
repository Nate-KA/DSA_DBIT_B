string = "data structures and algorithms"
freq = {}

for char in string:
    if char in freq:
        freq[char] = freq[char] + 1
    else:
        freq[char] = 1

for key, value in freq.items():
    print(f"'{key}': {value}")