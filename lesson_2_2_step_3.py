''' Задание: работа с выпадающим списком

Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
'''

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_xpath("//*[@id='num1']").text
    print(num1)

    num2 = browser.find_element_by_xpath("//*[@id='num2']").text
    print(num2)

    otvet = int(num1) + int(num2)
    print(otvet)

    select = Select(browser.find_element_by_xpath("//*[@id='dropdown']"))
    select.select_by_value(str(otvet))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
