import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.firefox.service import Service

@pytest.fixture
def browser():
    driver = webdriver.Firefox(service=Service(r'/home/karasik/git/test/geckodriver'))
    yield driver #после выполнения тест.функции будет выполнено след дей-вие
    driver.quit()

    
def test(browser):
    browser.get('https://sbis.ru')
    browser.find_element(By.LINK_TEXT, "Контакты").click()
    
    close_popup_window(browser)

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[4]/div[1]/div/div/div[2]/div/a").click()
    browser.switch_to.window(browser.window_handles[1])

    close_popup_window2(browser)

    wait = WebDriverWait(browser, 10)
    html_content = 'Сила в людях'
    xpath_expression = f"//*[contains(text(), '{html_content}')]"
    a = wait.until(EC.presence_of_element_located((By.XPATH, xpath_expression)))
    assert a, ("Элемент 'Сила в людях' не найден на странице.")

    try:
        company_block = browser.find_elements(By.LINK_TEXT, 'Сила в людях')
    except: 
        assert company_block, ("Блок 'Сила в людях' не найден на странице.")

    a = browser.find_element(By.XPATH, "//*[contains(text(), 'Сила в людях')]")
    parent_block = a.find_element(By.XPATH, '..')

    try:
        parent_block.find_element(By.LINK_TEXT, 'Подробнее').click() 
    except:
        print('Ссылка не открывается')

    b = browser.find_element(By.XPATH, "//*[contains(text(), 'Работаем')]")
    parent_block = b.find_element(By.XPATH, '../..')

    png_elements = parent_block.find_elements(By.XPATH, ".//img")
    
    #определение размеров изображений
    # for image in png_elements:
    #     width = image.get_attribute('width')
    #     height = image.get_attribute('height')
    #     print(f"Ширина: {width}, Высота: {height}")

    all_elements_equal = True
    for i in range(len(png_elements)):
        for j in range(i + 1, len(png_elements)):
            width_i = png_elements[i].get_attribute('width')
            height_i = png_elements[i].get_attribute('height')
            
            width_j = png_elements[j].get_attribute('width')
            height_j = png_elements[j].get_attribute('height')

            if width_i != width_j or height_i != height_j:
                all_elements_equal = False
                # diff = (f"Размеры для элементов {i} и {j} различаются.")
    assert all_elements_equal, ("Размеры изображений не совпадают")

def close_popup_window(driver):
    banner_element = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "sbis_ru-CookieAgreement__close"))
    )
    banner_element.click()
    pass

def close_popup_window2(driver):
    banner_element = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[3]/div[2]/div[2]"))
    )
    banner_element.click()
