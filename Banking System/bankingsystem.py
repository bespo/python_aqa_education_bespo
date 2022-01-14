"""Final Banking system"""

import sqlite3
import sys
from random import randint


class BankingSystem:
    """Bank System"""

    def __init__(self):
        self.state = "on"
        self.card_num = []
        self.card_pin = []
        self.user = None
        self.balance = None
        self.iin = 400000
        self.attempt = 0
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS card(
        id INTEGER PRIMARY KEY,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0)
        """)
        self.conn.commit()

    def main_menu(self):
        """Show menu"""
        print("\n1. Create an account\n"
              "2. Log into account\n"
              "0. Exit")

    def start_banking(self):
        """Main menu actions"""
        while True:
            self.main_menu()
            main_menu_selection = str(input())
            if main_menu_selection == "1":
                self.create_account()
            if main_menu_selection == "2":
                self.account_login()
            if main_menu_selection == "0":
                print('\nBye!')
                sys.exit()
            else:
                print('\nWrong card number or PIN!')

    def odd_multiply(self, numbers):
        for i in range(1, len(numbers) + 1):
            if i % 2 != 0:
                numbers[i - 1] *= 2
        return numbers

    def luhn_algorithm(self, iin, can):
        str_15_digits = f'{iin}{can}'
        numbers = list(map(lambda x: int(x), str_15_digits))
        odd_by_two = self.odd_multiply(numbers)
        subtracted = map(lambda x: x - 9 if x > 9 else x, odd_by_two)
        checksum = sum(subtracted)
        control_n = 10 - (checksum % 10)
        return control_n if control_n < 10 else 0

    def create_account(self):
        """Create account: card and pin"""
        customer_account_number = ''.join(f'{randint(0, 9)}' for _ in range(9))
        checksum = self.luhn_algorithm(self.iin, customer_account_number)
        self.card_num = f'{self.iin}{customer_account_number}{checksum}'
        self.card_pin = ''.join(f'{randint(0, 9)}' for _ in range(4))

        self.cur.execute(f"""INSERT INTO card (number, pin)
        VALUES ("{self.card_num}", "{self.card_pin}")""")
        self.conn.commit()

        print(f"\nYour card has been created\nYour card number: \n{self.card_num}\n"
              f"Your card PIN: \n{self.card_pin}\n")
        self.start_banking()

    def account_login(self, account_card, account_pin):
        """Login into account"""
        self.cur.execute(f"""SELECT * FROM card
        WHERE number = {account_card} AND pin = {account_pin}""")
        account = self.cur.fetchone()
        if account:
            self.attempt = 0
            self.user = account_card
            print("\nYou have successfully logged in!\n")
            self.user_action()
        else:
            self.attempt += 1
            print("\nWrong Card or PIN!\n")
            self.start_banking()

    def check_card_created(self):
        """Check the card in DB"""
        created_card = self.cur.execute(f"""SELECT number FROM card
        WHERE number = {self.card_num}""")
        if len(created_card.fetchall()) == 0:
            return False
        else:
            return True

    def card_menu(self):
        """Show card menu"""
        print("""Choose an option:
                1. Balance
                2. Add income
                3. Do transfer
                4. Close account
                5. Log out
                0. Exit
                    """)

    def user_action(self, action):
        balance = self.balance_account()
        if action == "1":
            print(f"\nBalance: {balance}\n")
        elif action == "2":
            self.add_income()
        elif action == "3":
            self.do_transfer()
        elif action == "4":
            self.close_account()
        elif action == "5":
            print("\nYou have successfully logged out!")
            self.start_banking()
        elif action == "0":
            print("Thank you for visiting!")
            self.conn.close()
            sys.exit()

    def balance_account(self):
        """Balance view"""
        balance = self.cur.execute(f'''SELECT balance FROM card WHERE number = {self.user}''')
        self.balance = balance.fetchone()[0]
        return self.balance

    def add_income(self, amount):
        """Add money to the card"""
        amount = int(amount) + self.balance_account()
        self.cur.execute(f"UPDATE card SET balance = {amount} WHERE number= {self.user}")
        self.conn.commit()
        print("Income was added!")
        self.user_action()

    def do_transfer(self, entered_value):
        """Transfer money to the card"""
        print("Enter how much money you want to transfer:")
        card_amount = input("> ")
        if self.check_card(entered_value, card_amount):
            card_amount = int(card_amount)
            self.balance -= card_amount
            self.cur.execute(f"UPDATE card SET balance = balance - "
                             f"({card_amount}) WHERE number = {self.user}")
            self.cur.execute(f"UPDATE card SET balance = balance + "
                             f"({card_amount}) WHERE number = {entered_value}")
            self.conn.commit()
            print("\nSuccess!")
        else:
            print("\nSuch a card does not exist!")
        self.user_action()

    def check_card(self, card_numbers):
        if len(card_numbers) == 16 and card_numbers.isdigit() is False:
            print("\nProbably you made mistake in the card number. Please try again!")
        elif card_numbers == self.user:
            print("\nYou can't transfer money to the same account!")
        elif not self.luhn_algorithm(card_numbers):
            print("\nLUHN CHECK: Probably you made a mistake in the card number.\nPlease try again!\n")
        else:
            return

    def check_card_amount(self, card_amount):
        if card_amount.isdigit() is False and int(card_amount) > 0:
            print("\nIncorrect amount!")
        elif int(card_amount) > self.balance:
            print("\nNot enough money!")
        else:
            return True

    def close_account(self):
        """Close the account"""
        self.cur.execute(f"DELETE FROM card WHERE number = {self.user}")
        self.conn.commit()
        self.user = None
        print("The account has been closed!")


def main():
    bs = BankingSystem()

    while True:
        if not bs.start_banking():
            break
        elif bs.state == "off":
            break


if __name__ == '__main__':
    main()
