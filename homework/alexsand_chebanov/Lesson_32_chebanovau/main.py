import requests
import time


def checkout_status_200(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Сайт {url} доступен')
    else:
        print(f'Сайт {url} недоступен. Статус код: {response.status_code}')


def main():
    url = "https://www.google.ru/"
    check_interval = 5
    while True:
        checkout_status_200(url)
        time.sleep(check_interval)


if __name__ == "__main__":
    main()
