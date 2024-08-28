from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

def startBot(username, password, url):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)

    print("Try to login")
    driver.get(url)
    driver.find_element(
        value="username").send_keys(username)
    driver.find_element(
        value="continue").click()
    driver.find_element(
        value="password").send_keys(password)
    driver.find_element(
        value="login").click()
    time.sleep(3)

    if "incorrect" in driver.page_source:
        print("Incorrect credentials!")
        return

    driver.get(url)
    time.sleep(3)

    if "Anda telah terhubung" in driver.page_source:
        print("Done login")
    else:
        print("Last loaded page")
        print("===================================================")
        print(driver.page_source)
        print("===================================================")
        print("Login failed, please try again!")

# Enter below your login credentials
username = "5024xxxxxx"
password = "password"

url = "https://myits-app.its.ac.id/internet/auth.php"

startBot(username, password, url)