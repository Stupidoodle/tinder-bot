from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    accept_cookies = driver.find_element(By.ID, "L2AGLb")
    accept_cookies.click()
    driver.quit()

if __name__ == "__main__":
    main()