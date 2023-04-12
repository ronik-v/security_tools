from socket import gethostbyname, gaierror, socket
from threading import Thread, ThreadError


class Scaner:
    ports = [0, 1, 2, 3, 5, 7, 9, 11, 13, 17, 18, 19, 20, 21, 22, 23, 24, 25,
             27, 29, 31, 35, 53, 79, 80, 88, 106, 110, 111, 113, 119, 139, 143,
             311, 312, 389, 427, 443, 445, 464, 465, 514, 515, 532, 548, 554, 587, 687, 1220]
    thread_ports_1 = ports[:len(ports) // 2]
    thread_ports_2 = ports[len(ports) // 2:]

    @classmethod
    def site_ip(cls, url: str) -> str:
        try:
            return gethostbyname(url)
        except gaierror as error:
            return f'Invalid URL: {error}'

    @classmethod
    def scan(cls, ip: str, port: int) -> None:
        if 'Invalid' in ip:
            exit(1)
        _socket = socket()
        try:
            _socket.settimeout(0.7)
            _socket.connect((ip, port))
            print(f'{ip} port: {port} is open')
        except BaseException:
            print(f'{ip} port: {port} is close')
        finally:
            _socket.close()

    @classmethod
    def scan_all(cls, ip: str, ports: list[int]) -> None:
        for port in ports:
            cls.scan(ip, port)

    @classmethod
    def up(cls, ip: str) -> None:
        thread_pool = list()
        try:
            thread_1 = Thread(target=cls.scan_all(ip, cls.thread_ports_1), args=(1,))
            thread_1.start()
            thread_2 = Thread(target=cls.scan_all(ip, cls.thread_ports_2), args=(2,))
            thread_2.start()

            for th in thread_pool:
                th.join()
        except ThreadError as error:
            print(error)
            exit(1)


def main() -> None:
    ip = str(input('Enter site URL or IP: '))
    Scaner.up(ip)


if __name__ == '__main__':
    main()
