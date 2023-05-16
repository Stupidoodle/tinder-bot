from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
import time
import keys

def main():
    driver = webdriver.Chrome()
    driver.get("https://tinder.com")
    driver.implicitly_wait(1)
    accept_cookies = driver.find_element(By.XPATH, "//div[text()='I accept']")
    accept_cookies.click()
    login = driver.find_element(By.XPATH, "//div[text()='Log in']")
    login.click()
    time.sleep(3)
    login = driver.find_element(By.XPATH, "//div[text()='Log in with phone number']")
    login.click()
    driver.implicitly_wait(1)

    while True:
        try:
            phone = driver.find_element(By.NAME, "phone_number")
            phone.send_keys(keys.phone)
            break
        except NoSuchElementException:
            time.sleep(5)

    cont = driver.find_element(By.XPATH, "//div[text()='Continue']")
    cont.click()
    driver.implicitly_wait(1)
    
    #Send email button automation
    while True:
        try:
            email = driver.find_element(By.XPATH, "//div[text()='Send email']")
            email.click()
            break
        except NoSuchElementException:
            time.sleep(5)

    while True:
        try:
            allow = driver.find_element(By.XPATH, "//div[text()='Allow']")
            allow.click()
            break
        except NoSuchElementException:
            time.sleep(5)

    not_i = driver.find_element(By.XPATH, "//div[text()='Not interested']")
    not_i.click()

    while True:
        try:
            profile = driver.find_element(By.XPATH, "//a[@role = 'img']")
            break
        except NoSuchElementException:
            time.sleep(5)

    while True:
        ActionChains(driver).send_keys(Keys.ARROW_RIGHT)
        time.sleep(5)

    driver.quit()

if __name__ == "__main__":
    main()