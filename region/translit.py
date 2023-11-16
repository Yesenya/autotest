from transliterate import translit

# Список регионов на русском
regions_russian = ['Москва', 'Санкт-Петербург', 'Уфа', 'Улан-Удэ', 'Горно-Алтайск', 'Махачкала', 'Назрань', 'Нальчик', 'Элиста', 'Черкесск', 'Петрозаводск', 'Сыктывкар', 'Саранск', 'Якутск', 'Владикавказ', 'Казань', 'Абакан', 'Грозный', 'Чебоксары', 'Барнаул', 'Краснодар', 'Красноярск', 'Владивосток', 'Ставрополь', 'Хабаровск', 'Архангельск', 'Астрахань', 'Белгород', 'Брянск', 'Владимир', 'Волгоград', 'Вологда', 'Воронеж', 'Иваново', 'Калининград', 'Калуга', 'Петропавловск-Камчатский', 'Кемерово', 'Кострома', 'Курган', 'Курск', 'Санкт-Петербург', 'Липецк', 'Магадан', 'Москва', 'Мурманск', 'Нижний Новгород', 'Великий Новгород', 'Новосибирск', 'Омск', 'Оренбург', 'Орел', 'Пенза', 'Пермь', 'Псков', 'Ростов-на-Дону', 'Рязань', 'Самара', 'Тольятти', 'Саратов', 'Южно-Сахалинск', 'Екатеринбург', 'Смоленск', 'Тамбов', 'Тверь', 'Томск', 'Тула', 'Тюмень', 'Ульяновск', 'Челябинск', 'Чита', 'Ярославль', 'Биробиджан', 'Запорожье', 'Севастополь', 'Донецк', 'Луганск', 'Херсон']

# Словарь для хранения соответствий
translit_dict = {}

# Заполняем словарь транслитерациями
for region in regions_russian:
    translit_dict[region] = translit(region, 'ru', reversed=True)

# Создаем список английских транслитераций
regions_english = [translit_dict[region] for region in regions_russian]

# Выводим результат
print(regions_english)