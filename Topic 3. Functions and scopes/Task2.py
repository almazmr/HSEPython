def trim_and_repeat(string, offset=0, repetitions=1):
    trimmed_string = string[offset:]
    repeated_string = trimmed_string * repetitions
    return repeated_string

result = trim_and_repeat("samsung", 3, 2)
print(result)

result = trim_and_repeat("apple", 3)
print(result)