"""
Goal of this code is to check if the response ist "hello", starts with "h"
or is somthing else. Based on this, you get money.
"Hello" = 0$
"H...." = 20$
else = 100$
"""


def main():
    money = how_much_money_do_you_get()
    print("$",money)


def how_much_money_do_you_get():
    word = str(input("Greeting: "))
    word = word.replace(" ", "")
    word = word.lower()

    if word.startswith("hello"):
        return 0
    elif word.startswith("h"):
        return 20 
    else:
        return 100

main()