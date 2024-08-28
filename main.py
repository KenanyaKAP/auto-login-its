from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

def startBot(username, password, url):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(options=op)

    driver.get(url)
    driver.find_element(
        value="username").send_keys(username)
    driver.find_element(
        value="continue").click()
    driver.find_element(
        value="password").send_keys(password)
    driver.find_element(
        value="login").click()

    if "incorrect" in driver.page_source:
        print("Incorrect credentials!")
    else:
        driver.get(url)
        if "Anda telah terhubung" in driver.page_source:
            print("Done login")
        else:
            print("Login failed, please try again")

# Enter below your login credentials
username = "50xxxxxxxx"
password = "password"

url = "https://myits-app.its.ac.id/internet/auth.php"

startBot(username, password, url)

print("Auto login ends")