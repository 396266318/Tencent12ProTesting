from selenium import webdriver
from time import sleep


def test_01():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    sleep(5)
    driver.quit()


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
sleep(5)
driver.quit()