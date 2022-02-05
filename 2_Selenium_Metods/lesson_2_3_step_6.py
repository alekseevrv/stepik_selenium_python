''' Задание: переход на новую вкладку

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ

'''

from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    print(browser.window_handles[0])

    button = browser.find_element_by_tag_name("button")
    button.click()

    print(browser.window_handles[1])

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_xpath("//*[@id='input_value']").text
    print(x)

    y = calc(x)

    otvet = browser.find_element_by_id('answer')
    otvet.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
