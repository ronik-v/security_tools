from os import system
from functools import cache
from datetime import datetime
from time import sleep
host_ip = '127.0.0.1'
hosts_way = r'C:\Windows\System32\drivers\etc\hosts'
sites = ['www.youtube.com', 'youtube.com', 'yandex.ru']


def main():
    date_to, date_from = get_dates()
    io_file(date_to, date_from)


def get_dates():
    date_to = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 9)
    date_from = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 18, 15)
    return date_to, date_from


@cache
def io_file(date_to, date_from):
    while True:
        system('ipconfig /flushdns')
        if date_to < datetime.now() < date_from:
            with open(hosts_way, 'r+') as file:
                src = file.read()
                for site in sites:
                    if site not in src:
                        file.write(f'{host_ip} {site}\n')
        else:
            with open(hosts_way, 'r+') as file:
                src = file.readlines()
                file.seek(0)

                for line in src:
                    if not any(site in line for site in sites):
                        file.write(line)
                file.truncate()
        sleep(5)


main()
