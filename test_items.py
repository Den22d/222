from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_multilanguage(browser):
    browser.get(link)
    time.sleep(5)
    x=browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert x,"NO BUTTON!!!"


    time.sleep(5)