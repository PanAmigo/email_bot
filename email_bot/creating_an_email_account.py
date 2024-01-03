import random
import time
import generators
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from pathlib import Path



gecodriver_path = Path("geckodriver.exe").resolve()
logins_psswd_path = Path("loginy_i_hasla.csv").resolve()

s = Service(gecodriver_path)
driver = webdriver.Firefox(service=s)
login_and_psswd_df = pd.read_csv(logins_psswd_path, delimiter=',')

def create_account():
    driver.get('http://www.onet.pl') #otwarcie przeglądarki
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'button.cmp-button_button:nth-child(2)').click() #akceptowanie cookies
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,'li.headerNavItem:nth-child(5) > a:nth-child(1)').click() #przejście do poczty
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.createAccount').click() #wybranie utworzenia nowego konta

    new_email = generators.generate_email()
    driver.find_element(By.XPATH,'//*[@id="alias"]').send_keys(new_email) #generowanie adresu
    driver.find_element(By.CSS_SELECTOR,'button.Button__ButtonStyled-sc-1d4cqpw-0:nth-child(1)').click()
    time.sleep(2)

    psswd = generators.generate_psswd() #tworzenie hasła
    driver.find_element(By.CSS_SELECTOR,'#newPassword').send_keys(psswd)
    driver.find_element(By.CSS_SELECTOR,'#rePassword').send_keys(psswd)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,'button.Button__ButtonStyled-sc-1d4cqpw-0:nth-child(3)').click()

    driver.find_element(By.XPATH,'//*[@id="recoveryEmail"]').send_keys(generators.generate_second_mail()) #uzupełnienie adresu pomocniczego jako mail do odzyskania hasła
    driver.find_element(By.CSS_SELECTOR,'.Button__ButtonStyled-sc-1d4cqpw-0').click()
    time.sleep(2)

    #rejestracja uzupełnianie danych
    driver.find_element(By.XPATH, '//*[@id="name"]').clear()
    driver.find_element(By.XPATH,'//*[@id="name"]').send_keys(generators.generate_name() + " " + generators.generate_surname()) #imie i nazwisko
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[1]/div/div[2]/label/span').click() #ustawienie tytuł
    driver.find_element(By.XPATH,'//*[@id="birthDate.day"]').send_keys(generators.generate_day()) #losowy dzień
    driver.find_element(By.XPATH,'//*[@id="birthDate.month"]').click() #rozwinięcie listy z miesiącami
    all_options = driver.find_elements(By.TAG_NAME,"option") #pobranie listy miesięcy
    all_options.remove(all_options[0]) #usunięcie opcji pierwszej "miesiąc"
    random.choice(all_options).click() #wybranie losowo miesiąca
    driver.find_element(By.XPATH,'//*[@id="birthDate.year"]').send_keys(generators.generate_year()) #uzupełnianie roku
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR,'.Button__ButtonStyled-sc-1d4cqpw-0').click() #dalej
    time.sleep(2)

    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div/div/div[3]/button/span[1]').click() #wybór pakietu
    time.sleep(2)

    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[1]/button').click() #zaakceptowanie regulaminów
    time.sleep(2)

    try:
        driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div/div/form/div[2]/div/button/span[1]').click() #przejście dalej
    except:
        print('coś poszło nie tak, spróbuj ponownie później')
        exit()
    else:
        next_mail = [new_email, psswd]
        login_and_psswd_df.loc[len(login_and_psswd_df)] = next_mail
        login_and_psswd_df.to_csv(r"D:\PythonProjects\projekt zaliczenie\loginy_i_hasla.csv", index=False, index_label=False) #zapisanie zmian w csv
        driver.quit()

def quit_driver():
    driver.quit()
