''' Загрузка файлов

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"

'''

from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//input[@name='firstname']")
    input1.send_keys('Ivan')

    input2 = browser.find_element_by_xpath("//input[@name='lastname']")
    input2.send_keys('Ivanov')

    input3 = browser.find_element_by_xpath("//input[@name='email']")
    input3.send_keys('email@email.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '_info.txt')
    input_file = browser.find_element_by_xpath("//input[@id='file']")
    input_file.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
