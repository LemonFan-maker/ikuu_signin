from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os
import sys

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-blink-features')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=chrome_options)

Email01 = os.environ.get('Email01')
Pass01 = os.environ.get('Pass01')

driver.get("https://ikuuu.pw/auth/login")
sleep(5)
driver.find_element(By.XPATH, "/html/body/div[1]/section/div/div/div/div[2]/form/div/div[1]/input").send_keys(str(Email01))
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/section/div/div/div/div[2]/form/div/div[2]/input").send_keys(str(Pass01))
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/section/div/div/div/div[2]/form/div/div[5]/button").click()
sleep(5)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/button[1]").click()
sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/section/div[1]/div/div/a").click()
sleep(5)
driver.close()

