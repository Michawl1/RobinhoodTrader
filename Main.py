"""
@author Michael Thompson (mjt106@case.edu)
@details This is the main file for a python trader that interfaces with robinhood
"""

import robin_stocks as r
import getpass
import sys

if __name__ == "__main__":
    print("Enter username: ")
    username = input()

    if sys.stdin.isatty():
        password = getpass.getpass(prompt='Enter password: ')
    else:
        print("Enter password: ")
        password = sys.stdin.readline().rstrip()

    login = r.login(username, password)

    my_stocks = r.build_holdings()

    print(my_stocks)
