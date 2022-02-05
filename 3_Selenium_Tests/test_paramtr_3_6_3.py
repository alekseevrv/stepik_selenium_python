""" Задание: параметризация тестов

Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение.
Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений.
Ваша задача — реализовать автотест со следующим сценарием действий:

открыть страницу
ввести правильный ответ
нажать кнопку "Отправить"
дождаться фидбека о том, что ответ правильный
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

"The owls are not what they seem! OvO"

"""

import pytest
import time
import math

from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('site', [
    "236895/step/1",
    "236896/step/1",
    "236897/step/1",
    "236898/step/1",
    "236899/step/1",
    "236903/step/1",
    "236904/step/1",
    "236905/step/1"
])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, site):
        link = f"https://stepik.org/lesson/{site}/"

        # неявное ожидание
        browser.implicitly_wait(10)

        browser.get(link)
        answer = math.log(int(time.time()))
        print(answer)

        textarea = browser.find_element_by_xpath("//textarea")
        textarea.send_keys(str(answer))

        button = browser.find_element_by_xpath("//button[@class ='submit-submission']")
        button.click()

        otvet = browser.find_element_by_xpath("//*[@class='smart-hints__hint']")
        print("++" + otvet.text + "++")

        assert otvet.text == "Correct!", "Ответ не тот"
