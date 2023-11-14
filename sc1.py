from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 

driver = webdriver.Firefox(executable_path=r'/home/karasik/git/test/geckodriver')
driver.get('https://sbis.ru')
driver.find_element(By.LINK_TEXT, "Контакты").click()


# вспылающее о куки
banner_element = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "sbis_ru-CookieAgreement__close"))
)
banner_element.click()
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/div/div/div[2]/div/a").click()


# all_handles = driver.window_handles
# driver.switch_to.window(all_handles[-1])
# переключение на новую вкладку(необязательно)
driver.switch_to.window(driver.window_handles[1])

# закрытие всплывающего с помощью Xpath
# banner_element = WebDriverWait(driver,10).until(
#     EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[3]/div[2]/div[2]"))
# )
# banner_element.click()

# закрытие всплывающего с помощью Css селектора 
banner_element = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".tensor_ru-CookieAgreement__close"))
)
banner_element.click()

# проверяем наличие блока с текстом, если его нет, то пишем что его нет
try:
    company_block = driver.find_elements(By.LINK_TEXT, 'Сила в людях')
except: 
    print("Блок 'Сила в людях' не найден на странице.")

# Находим блок с нужным названием, перемещаемся на путь выше '..' находим атрибуты 
# родительского блока, находим в них элемент с нужным названием
a = driver.find_element(By.XPATH, "//*[contains(text(), 'Сила в людях')]")
parent_block = a.find_element(By.XPATH, '..')
# print("Родительский блок:", parent_block.get_attribute('outerHTML'))
try:
    element_in_block = parent_block.find_element(By.LINK_TEXT, 'Подробнее').click() 
except:
    print('Ссылка не открывается')

# Находим блок с нужным названием, перемещаемся на 2 уровня выше '../..' находим 
# атрибуты родительского блока
b = driver.find_element(By.XPATH, "//*[contains(text(), 'Работаем')]")
parent_block = b.find_element(By.XPATH, '../..')
# print("Родительский блок:", parent_block.get_attribute('outerHTML'))

png_elements = parent_block.find_elements(By.XPATH, ".//img")
# first_elements = parent_block.find_elements(By.XPATH, ".//img[0]")
# width_1 = first_elements.get_attribute('width')
# height_1 = first_elements.get_attribute('height')

# говнокод, надо бы исправить, но работает
# first_image = parent_block.find_element(By.TAG_NAME, 'img')
# width_1 = first_image.get_attribute('width')
# height_1 = first_image.get_attribute('height')
# i = 0
# for element in png_elements:
#     width = element.get_attribute('width')
#     height = element.get_attribute('height')
#     i +=1
#     if width_1 == width and height_1 == height:
#         None
#     else:
#         print('Изображение № {} - отличается по размеру'.format(i))

# вариант получше
for i in range(len(png_elements)):
    for j in range(i + 1, len(png_elements)):
        width_i = png_elements[i].get_attribute('width')
        height_i = png_elements[i].get_attribute('height')
        
        width_j = png_elements[j].get_attribute('width')
        height_j = png_elements[j].get_attribute('height')

        if width_i == width_j and height_i == height_j:
            None # либо написать условие, что совпадает размер
        else:
            print(f"Размеры для элементов {i} и {j} различаются.")
    


# driver.refresh()
# driver.quit()
