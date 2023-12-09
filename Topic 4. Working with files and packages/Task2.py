import csv
import json

# Создаем словарь с категориями покупок из файла purchase_log.txt
purchases = {}
with open('purchase_log.txt', 'r', encoding='utf-8') as purchase_file:
    for line in purchase_file:
        data = json.loads(line)
        if 'user_id' in data and 'category' in data:
            purchases[data['user_id']] = data['category']

# Читаем файл visit_log.csv и записываем в файл funnel.csv только визиты с покупками и их категориями
with open('visit_log.csv', 'r', encoding='utf-8') as visit_file, open('funnel.csv', 'w', encoding='utf-8', newline='') as funnel_file:
    visit_reader = csv.reader(visit_file)
    funnel_writer = csv.writer(funnel_file)
    
    # Записываем заголовок в файл funnel.csv
    funnel_writer.writerow(['user_id', 'source', 'category'])
    
    # Обрабатываем каждую строку в файле visit_log.csv
    for row in visit_reader:
        user_id = row[0]
        source = row[1]
        
        # Проверяем, есть ли у данного user_id категория покупки в словаре purchases
        if user_id in purchases:
            category = purchases[user_id]
            funnel_writer.writerow([user_id, source, category])