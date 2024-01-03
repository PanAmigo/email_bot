import random
import time
import generators
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from pathlib import Path
from selenium.webdriver.common.keys import Keys


gecodriver_path = Path("geckodriver.exe").resolve()

s = Service(gecodriver_path)
driver = webdriver.Firefox(service=s)


driver.get('https://www.komoot.com/discover/Warsaw/@52.2319237%2C21.0067265/tours?sport=touringbicycle&distance=16.1')  # otwarcie przeglądarki
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '.css-8j99ff').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[2]/div/div[3]/div/div/div/form/input').send_keys("warszawa")  # generowanie adresu
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[2]/div/div[3]/div/div/div/form/input').send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '.css-8j99ff').click()
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[2]/div/div[3]/div/div/div/form/input').send_keys("poznan")