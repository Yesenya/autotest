
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.firefox.service import Service
import http.client
import requests


@pytest.fixture
def browser():
    driver = webdriver.Firefox(service=Service(r'/home/karasik/git/test/geckodriver'))
    yield driver
    driver.quit()

def test_two(browser):
    browser.get('https://sbis.ru')
    browser.find_element(By.LINK_TEXT, "Контакты").click()

    close_pop_up_m(browser)

    el = browser.find_element(By.CLASS_NAME, "sbis_ru-Region-Chooser")
    assert el, ("Регион не отображается")
    txt_cnt = el.text 
    # with open ("result.txt") as f:
    #     f_cnt = f.read(user_region)
    reg = region_by_ip() 
  

    print ("Сравни регионы: - {}, согласно сайту: {}".format(reg, txt_cnt))
    
    # print(f"Сравни регионы: действительный - {}, на сайте - {}")

    assert browser.find_element(By.CSS_SELECTOR, "div.controls-Tree__item:nth-child(2)"),("Партнеры не отображаются")

    try:
        browser.find_element(By.CLASS_NAME, "sbis_ru-Region-Chooser").click()
        botton_clicked= browser.find_element(By.CSS_SELECTOR, 'span[title="Камчатский край"]').click()

    except:
        assert ("Не прожимается кнопка")
    
    assert browser.find_element(By.CLASS_NAME, "sbis_ru-Region-Chooser"), ("Регион не отображается")
    assert browser. find_element(By.CSS_SELECTOR, "div.controls-Tree__item:nth-child(2)"), ("Партнеры не отображаются")

def close_pop_up_m(driver):
    banner_element = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "sbis_ru-CookieAgreement__close"))
    )
    banner_element.click()



def region_by_ip():
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    ip = conn.getresponse().read()
    fixed = ip.decode("utf-8").strip()

    def get_user_region(ip):
        try:
            response = requests.get(f"https://ipinfo.io/{ip}/json?lang=ru")
            data = response.json()
            return data.get("region")
        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")
            return None
        
    user_region = get_user_region(fixed)
    return {"user_region": user_region}









