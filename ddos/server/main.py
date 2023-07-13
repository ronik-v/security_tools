from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread, ThreadError
from sys import argv


def create_socket_stream(ip_array: list[str], attacked_host: bytes, port=2999) -> None:
	with socket(AF_INET, SOCK_STREAM) as _soc:
		for ip in ip_array:
			_soc.connect((ip, port))
			_soc.send(attacked_host)
			data_buffer = _soc.recv(1024)
			print(f'[+] Received [{attacked_host.decode("utf-8")}] to -> {ip}')
		_soc.close()


def main() -> None:
	ip_to_attack: list[str] = ['']
	slice_to: int = len(ip_to_attack) >> 1
	attacked_host_url: bytes = argv[1].encode('utf-8')
	pool: list[Thread] = list()
	try:
		thread1, thread2 = Thread(target=create_socket_stream, args=(ip_to_attack[:slice_to], attacked_host_url,)), \
			Thread(target=create_socket_stream, args=(ip_to_attack[slice_to:], attacked_host_url,))
		thread1.start(); thread2.start()
		pool.append(thread1); pool.append(thread2)
		pool[0].join(); pool[1].join()
	except ThreadError as error:
		print(error)
		exit(1)



if __name__ == '__main__':
	main()
