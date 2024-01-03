from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

import time

gecodriver_path = Path("geckodriver.exe").resolve()
s = Service(gecodriver_path)
driver = webdriver.Firefox(service=s)

driver.get('https://www.komoot.com/discover/Lublin/@51.2505590%2C22.5701022/tours?sport=touringbicycle&distance=32.19')

cities = ['Lublin', 'Warszawa', 'Lodz']
amountOfRutes = []

#BclearCity = driver.find_element(By.TAG_NAME, 'button')
#clearCity = driver.find_element(By.CSS_SELECTOR, '.css-8j99ff')
searchCity = driver.find_element(By.CLASS_NAME, 'css-1444v67')
#searchButton = driver.find_element(By.CLASS_NAME, 'css-10gqc9r')
#rutesAmount = driver.find_element(By.XPATH,'//*[@id="pageMountNode"]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div/p/span/span')



for city in cities:

    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, '.css-8j99ff').click()
    #for x in range(30): searchCity.send_keys(Keys.BACKSPACE)
    time.sleep(3)

    searchCity.send_keys(city)
    time.sleep(3)

    searchCity.send_keys(Keys.ENTER)
    time.sleep(3)

    #print(rutesAmount.text)
    #searchCity.send_keys(Keys.BACKSPACE)

    #driver.refresh()#????

"""
    ruteRadious = driver.find_element(By.ID, 'radius-select')
    radiousOptions = driver.find_elements(By.TAG_NAME, 'option')

    for lenth in radiousOptions:
        ruteRadious.click()
        time.sleep(3)

        lenth.click()
        time.sleep(3)

        ruteRadious.click()

        time.sleep(5)
"""


time.sleep(10)

"""
#Pierwsza iteracja
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'css-8j99ff'))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'css-1444v67'))
    )
    element.send_keys(xd)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'css-10gqc9r'))
    )
    element.click()

except:
    driver.quit()
"""

driver.quit()
