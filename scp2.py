from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 
# import time

driver = webdriver.Firefox(executable_path=r'/home/karasik/git/test/geckodriver')
driver.get('https://sbis.ru')
driver.find_element(By.LINK_TEXT, "Контакты").click()
# тут тоже момент с всплывающим окном

# всплывающее окно
banner_element = WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "sbis_ru-CookieAgreement__close"))
)
banner_element.click()
# time.sleep(5)
# alert = driver.switch_to.alert
# alert.accept()

# banner_element = WebDriverWait(driver,10).until(
#     EC.visibility_of_element_located((By.CLASS_NAME, "sbis_ru-CookieAgreement__close"))
# )
# banner_element.click()

# проверка региона
try:
    #el = driver.find_element(By.CSS_SELECTOR, "html body.ws-is-firefox.ws-is-unix.ws-is-desktop-platform.ws-fix-emoji.zIndex-context.ws-is-no-touch.ws-is-no-drag.Application-body.controls_theme-sbisru.sbis_ru.sbis_ru-wasaby.theme--default.ws-body-no-scroll.ws-is-hover.sbis-ru-CookieAgreement-visible div#wasaby-content div div.bodyContent div.sbis_ru-Region.bodyContent__zIndex-context div.sbis_ru-content div.controls-Scroll-Container.controls-Scroll.controls_scroll_theme-sbisru.sbis_ru-content_scrollContainer div.controls-Scroll-ContainerBase.controls_scroll_theme-sbisru.controls-Scroll__content.controls-Scroll__content_hideNativeScrollbar.controls-Scroll__content_hideNativeScrollbar_ff-ie-edge.controls-Scroll-ContainerBase__scroll_vertical.controls-Scroll-ContainerBase__scrollPosition-regular.controls-Scroll-Container__base.controls-BlockLayout__blockGroup.undefined div.controls-Scroll-ContainerBase__content.controls-Scroll-ContainerBase__content__vertical.controls-Scroll-ContainerBase__content-direction_column div#container.controls-Scroll-containerBase_userContent div.sbis_ru-content_wrapper.ws-flexbox.ws-flex-column div.sbisru-Contacts div.sbis_ru-container.sbisru-Contacts__relative div.s-Grid-container.s-Grid-container--space.s-Grid-container--alignEnd.s-Grid-container--noGutter.sbisru-Contacts__underline div.s-Grid-col.s-Grid-col--xm12 div.s-Grid-container.s-Grid-container--alignBaseline.s-Grid-container--noGutter.pb-4.pb-xm-16.pr-16.pr-xm-0 div.s-Grid-col.s-Grid-col--xm12 span.sbis_ru-Region-Chooser.ml-16.ml-xm-0")
    el = driver.find_element(By.CLASS_NAME, "sbis_ru-Region-Chooser")
    print ("Регион отображается")
    # print (el)
except: 
    print ("Регион не отображается")

# проверка партнеров
try:
    el2 = driver.find_element(By.CSS_SELECTOR, "div.controls-Tree__item:nth-child(2)")
    print ("Партнеры отображаются")
except: 
    print ("Партнеры не отображаются")

# Меняем регион на Камчатский
driver.find_element(By.CLASS_NAME, "sbis_ru-Region-Chooser").click()
driver.find_element(By.CSS_SELECTOR, 'span[title="Камчатский край"]').click()

# <span class="sbis_ru-Region-Chooser__text sbis_ru-link">Камчатский край</span>

try:
    el = driver.find_element(By.CLASS_NAME, "sbis_ru-Region-Chooser")
    text_on_element = el.text
    #print(f"Текст на элементе: {text_on_element}")   
    el2 = driver.find_element(By.CSS_SELECTOR, "div.controls-Tree__item:nth-child(2)")
    print ("Партнеры отображаются")
except:
    None

# driver.quit()