import random
import string

import pandas as pd
from random import randrange
from pathlib import Path

names_path = Path("imiona.csv").resolve()
surnames_path = Path("nazwiska.csv").resolve()

names_df = pd.read_csv(names_path, sep=',')
surnames_df = pd.read_csv(surnames_path, sep=',')

random_name_index = randrange(len(names_df))
random_surname_index = randrange(len(surnames_df))

characters_password = list(string.ascii_letters + string.digits + "!@#$%^&*()")
characters_mail = list(string.ascii_letters + string.digits + "_")

def generate_name():
    return names_df["IMIĘ_PIERWSZE"].values[random_name_index]

def generate_surname():
    return surnames_df["NAZWISKO"].values[random_surname_index]

def generate_psswd():
    length = 8
    random.shuffle(characters_password)
    password = []
    psswd= ""

    for i in range(length):
        password.append(random.choice(characters_password))

    password.append("Ab1")
    random.shuffle(password)
    for char in password:
        psswd += char

    return psswd

def generate_email():
    length = 8
    random.shuffle(characters_mail)
    mail = []
    email = ""

    for i in range(length):
        mail.append(random.choice(characters_mail))

    random.shuffle(mail)
    for char in mail:
        email += char

    return email.lower()

def generate_second_mail():
    length = 8
    random.shuffle(characters_mail)
    mail = []

    for i in range(length):
        mail.append(random.choice(characters_mail))

    random.shuffle(mail)
    mail.append("@op.pl")
    return mail

def generate_day():
    day = randrange(1,28)
    return day

def generate_year():
    year = randrange(1950,2000)
    return year