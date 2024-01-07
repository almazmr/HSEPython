import re

def validate_car_id(car_id):
    pattern = r'^[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$'

    if re.match(pattern, car_id):
        number = car_id[:6]
        region = car_id[6:]
        return f'Номер {number} валиден. Регион: {region}.'
    else:
        return 'Номер не валиден'
    
car_id = 'А222ВС96'
result = validate_car_id(car_id)
print(result)  # Номер А222BС валиден. Регион: 96.

car_id = 'АБ22ВВ193'
result = validate_car_id(car_id)
print(result)  # Номер не валиден.