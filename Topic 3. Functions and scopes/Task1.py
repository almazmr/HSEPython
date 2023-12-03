def sum_distance(from_value, to_value):
    if from_value > to_value:
        from_value, to_value = to_value, from_value
    return sum(range(from_value, to_value+1))

result = sum_distance(1, 3)
print(result)

result = sum_distance(3, 1)
print(result)