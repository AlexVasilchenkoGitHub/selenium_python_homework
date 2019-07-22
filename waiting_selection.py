from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

price_bool = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))

if price_bool:
    btn = browser.find_element(By.ID, "book")
    btn.click()

    # считаем нужное значение математического выражения при полученном x
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    element_input = browser.find_element_by_css_selector("#answer")
    element_input.send_keys(y)

    option_rule = browser.find_element(By.ID, "solve")
    option_rule.click()



# закроет браузер
time.sleep(20)
browser.quit()
