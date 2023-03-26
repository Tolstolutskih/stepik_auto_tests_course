from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element(By.XPATH, '//button[text()="I want to go on a magical journey!"]')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x1 = browser.find_element(By.ID, "input_value")
    x = x1.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer" )
    input1.send_keys(y)
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()
   

    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла