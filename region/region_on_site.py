import re

file_path = 'data.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read()
    
    pattern = re.compile(r'city:i\("(.*?)"')
    pattern_2 = re.compile(r'shortName:i\("(.*?)"')

    cities = pattern.findall(data)
    regions = pattern_2.findall(data)

    cities = [city for city in cities if city]
    regions = [region for region in regions if region]

    print(cities)
    print (regions)

