import re


example_text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

сiv_pattern = r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b'
taxi_pattern = r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}\b'

civ_num = re.findall(сiv_pattern, example_text)
taxi_num = re.findall(taxi_pattern, example_text)

print('Список номеров частных автомобилей:', civ_num)
print('Список номеров такси:', taxi_num)