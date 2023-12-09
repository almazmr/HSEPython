import json

purshases = {}

with open('purchase_log.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line)
        if 'user_id' in data and 'category' in data:
            purshases[data['user_id']] = data['category']

for user_id, category in purshases.items():
    print(user_id, category)