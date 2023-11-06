import os
import time
import requests
import platform


def main():
    import logo

    time.sleep(1)

    print('1: Send sms')

    choices = input("\nChoose option: ")

    if choices == "1":
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

        time.sleep(1)
        print("(Ex. 111-111-1111)")
        smsnumb = input('Enter a phone number: ')
        message = input('Enter the message you want to send and press enter: ')
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
