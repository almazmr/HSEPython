import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with open('events.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['events'])

plt.figure(figsize=(10, 6))
sns.countplot(y='signature', data=df, order=df['signature'].value_counts().index)
plt.title('Распределение типов событий информационной безопасности')
plt.xlabel('Количество событий')
plt.ylabel('Тип события')
plt.show()