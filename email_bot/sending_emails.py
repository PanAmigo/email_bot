import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from pathlib import Path

gecodriver_path = Path("geckodriver.exe").resolve()
logins_psswd_path = Path("loginy_i_hasla.csv").resolve()

s = Service(gecodriver_path)
driver = webdriver.Firefox(service=s)
users_data_df = pd.read_csv(logins_psswd_path, delimiter=',')

def main():
    log_in_to_mail("", "")

def log_in_to_mail(login, psswd):
    if login == "" and psswd == "": #pobieranie danych ostaniego logowania ostatnio zakładanego konta
        series = users_data_df.iloc[-1].tolist()
        login, psswd = series


    driver.get('http://www.onet.pl')  # otwarcie przeglądarki
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'button.cmp-button_button:nth-child(2)').click()  # akceptowanie cookies
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'li.headerNavItem:nth-child(5) > a:nth-child(1)').click()  # przejście do poczty
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="mailFormLogin"]').send_keys(login + "@op.pl") #wpisujemy login
    driver.find_element(By.XPATH, '//*[@id="mailFormPassword"]').send_keys(psswd) #wpisujemy haslo
    try:
        driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/form/div[3]/input').click() #klikamy zaloguj
        time.sleep(2)
    except:
        print('nie udało się zalogować, spróbuj ponownie')
    else:
        print("udało się zalogować")

def send_mail(recipients, mail_title, msg):
    driver.find_element(By.XPATH, '/html/body/main/div/div[8]/div[3]/aside/div[1]/div/span/span/span').click() #wyślij wiadomość
    for person in recipients: #uzupełniamy odbiorców
        driver.find_element(By.CSS_SELECTOR, '.styles__BubbleField-sc-5np2wj-0').send_keys(person)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '.styles__BubbleField-sc-5np2wj-0').click()
        time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '.styles__FormInputField-mz1adf-0').send_keys(mail_title) #ustalamy tytuł
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#CONTENT_TEXTAREA_ID_ifr').send_keys(msg) #wpisujemy treść wiadomości
    driver.find_element(By.CSS_SELECTOR, '.evlwod > span:nth-child(1) > span:nth-child(2)').click() #klikamy wyślij

    time.sleep(10)
    print('pomyślnie udało się wysłać wiadomości')
    driver.quit()