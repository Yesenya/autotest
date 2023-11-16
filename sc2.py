import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.firefox.service import Service

@pytest.fixture
def browser():
    driver = webdriver.Firefox(service=Service(r'/home/karasik/git/test/geckodriver'))
    yield driver
    driver.quit()

def test_two(browser):
    browser.get('https://sbis.ru')
    browser.find_element(By.LINK_TEXT, "Контакты").click()

    close_pop_up_m(browser)

     # проверка региона
    
    el = browser.find_element(By.CLASS_NAME, "sbis_ru-Region-Chooser")
    assert el, ("Регион не отображается")
    # el
    
    # print(f"Сравни регионы: действительный - {}, на сайте - {}")

    # проверка партнеров

    assert browser.find_element(By.CSS_SELECTOR, "div.controls-Tree__item:nth-child(2)"),("Партнеры не отображаются")
    # print ("Партнеры отображаются")
    
    # Меняем регион на Камчатский
    browser.find_element(By.CLASS_NAME, "sbis_ru-Region-Chooser").click()
    browser.find_element(By.CSS_SELECTOR, 'span[title="Камчатский край"]').click()
    # <span class="sbis_ru-Region-Chooser__text sbis_ru-link">Камчатский край</span>

    # сделать функции что для того что выше, что для того что ниже
    el = browser.find_element(By.CLASS_NAME, "sbis_ru-Region-Chooser")
    text_on_element = el.text
    #print(f"Текст на элементе: {text_on_element}")   
    el2 = browser. find_element(By.CSS_SELECTOR, "div.controls-Tree__item:nth-child(2)")
    # print ("Партнеры отображаются")


def close_pop_up_m(driver):
    banner_element = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "sbis_ru-CookieAgreement__close"))
    )
    banner_element.click()

   









