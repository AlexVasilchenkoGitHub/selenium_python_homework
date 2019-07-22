'''
https://stepik.org/lesson/36285/step/13?unit=162401
'''
from selenium import webdriver
import unittest
import time

def common_test(browser):

    element_1 = browser.find_element_by_xpath("//div[contains(@class, 'first_block')]//div[contains(@class, 'form-group')]//input[contains(@class, 'first')]")
    element_1.send_keys("any answer")
    element_2 = browser.find_element_by_xpath("//div[contains(@class, 'first_block')]//div[contains(@class, 'form-group')]//input[contains(@class, 'second')]")
    element_2.send_keys("any answer")
    element_3 = browser.find_element_by_xpath("//div[contains(@class, 'first_block')]//div[contains(@class, 'form-group')]//input[contains(@class, 'third')]")
    element_3.send_keys("any answer")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    return welcome_text_elt.text


class TestAbs(unittest.TestCase):

    def test_first_page(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        welcome_text = common_test(browser)
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)

    def test_second_page(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        welcome_text = common_test(browser)
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)

if __name__ == "__main__":
    unittest.main()
