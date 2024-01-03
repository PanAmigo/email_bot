import creating_an_email_account
import sending_emails

def main():
    step1_newemail_or_oldone()
    declare_msg()

def yes_no(question):
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response

def step1_newemail_or_oldone():
    new_email = yes_no("Czy chcesz założyć nowy email? (t/n): ")
    if new_email == "t":
        print("Daj mi chwilke")
        creating_an_email_account.create_account()
        print("zrobione, zaczynam logowanie")
        sending_emails.log_in_to_mail("", "")
    else:
        creating_an_email_account.quit_driver()
        print("podaj email (z domeny @op.pl) z jakiego chcesz skorzystać, aby skorzystać z ostatnio wygenerowanego zostaw puste dane")
        email = input()
        print('podaj haslo do poczty')
        psswd = input()
        print("dzieki, daj mi chwile")
        sending_emails.log_in_to_mail(email, psswd)

def declare_msg():
    is_it_the_last_recipient = 'n'
    recipients = []
    while is_it_the_last_recipient == 'n':
        print("podaj email odbiorcy")
        recipients.append(input())
        is_it_the_last_recipient = yes_no('czy to ostatni?')
    else:
        print('podaj tytul wiadomosci')
        title = input()
        print('podaj tresc wiadomosci')
        msg = input()
        sending_emails.send_mail(recipients, title, msg)

main()
exit()
