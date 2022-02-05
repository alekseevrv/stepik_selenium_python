""" Задание: оформляем тесты в стиле unittest

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element
из библиотеки expected_conditions.
-------------------------------------
Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194 (lesson_1_6_step_11.py)
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
Отправьте эту строчку в качестве ответа на это задание
Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте.
Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо
(во всяком случае, здесь)!
"""

from selenium import webdriver
import time
import unittest


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
        input1.send_keys("Ivan")

        input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
        input2.send_keys("Ivanov")

        input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @required]")
        input3.send_keys("Ivanovich")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration false")

        time.sleep(10)
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
        input1.send_keys("Ivan")

        input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
        input2.send_keys("Ivanov")

        input3 = browser.find_element_by_xpath("//input[@class='form-control third' and @required]")
        input3.send_keys("Ivanovich")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration false")

        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
