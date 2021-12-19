"""Final Text Browser"""

import sys
from collections import deque

import requests
from bs4 import BeautifulSoup
from colorama import Fore


class TextBrowser:
    """Text Browser"""
    current_page = "There is no history anymore"
    directory = None

    def __init__(self):
        self.history = deque()

    def save_page_content(self, name, content):
        """Save page content"""
        with open(name, "w", encoding="utf-8") as f:
            f.write(content)

    def show_name_content(self):
        """Show last name URL"""
        name = self.get_previous_page()
        print(name)

    def get_user_input(self):
        """User input"""
        while True:
            command = input()
            if command:
                return command

    def is_url(self, command):
        """Check URL"""
        return "." in command

    def add_to_history(self, content):
        """Add content to history"""
        self.history.append(content)

    def get_previous_page(self):
        """Return the last url"""
        return self.history.pop()

    def get_page_content(self, url):
        """Enter URL"""
        response = requests.get(url if "https://" in url else "https://" + url,
                                headers={"user-agent": "Mozilla/5.0"}, timeout=5)
        return response

    def handle_url(self, url):
        """Data processing"""
        try:
            content = self.get_page_content(url)
            # print(content.text)
            # print(content.text[:30])
            # add_to_history(content.text)

        except Exception:
            print("Not valid URL")

        else:
            try:
                self.add_to_history(self.current_page)
                self.current_page = url
                self.save_page_content(url.split('.')[0], content.text)
                self.print_page_content(self.get_page_content(url))
            except Exception:
                print("Something goes wrong")

    def go_back(self):
        """Show previous page"""
        page = self.get_previous_page()
        print(page)

    def print_page_content(self, response):
        """Output and color the required tags"""
        soup = BeautifulSoup(response.content, "html.parser")
        tags = ["p", "h1", "h2", "h3", "h4", "h5", "h6", "a", "ul", "ol", "li"]
        page = soup.find_all(tags)
        # print(page)
        for tag in page:
            text = tag.get_text()
            if tag.name == "a" and "href" in tag.attrs:
                print(Fore.BLUE + text)
            else:
                print(Fore.GREEN + text)
            print(Fore.RESET)

    def show_menu(self):
        """Select menu"""
        print("1.Enter URL\n2.Back\n3.Exit")


TB = TextBrowser()


def main():
    """Actions"""
    while True:
        TB.show_menu()
        print("Please select an option")
        command = TB.get_user_input()
        if command == "1":
            while True:
                print("Please enter URL")
                url = TB.get_user_input()
                if TB.is_url(url):
                    TB.handle_url(url)
                    break
                else:
                    print("URL is incorrect\n")
                    continue
        elif command == "2":
            TB.show_name_content()
            # go_back()
        elif command == "3":
            sys.exit()
        else:
            print("Incorrect input")


if __name__ == "__main__":
    main()
