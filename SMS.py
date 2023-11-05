import os
import time
import requests
import platform


def main():
    import logo

    time.sleep(1)

    print('1: Send sms')

    choices = input("\nPlease choice: ")

    if choices == "1":
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

        time.sleep(1)
        smsnumb = input("Input the number of the target: ")
        message = input("Please input the message: ")

        resp = requests.post('https://textbelt.com/text', {
            'phone': f'{smsnumb}',
            'message': f'{message}',
            'key': 'textbelt',
        })

        print(resp.json())
        time.sleep(5)

        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

        return main()

    elif choices == "3":
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

main()