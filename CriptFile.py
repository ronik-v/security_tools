from os import system
from sys import exit, platform
import threading
import rsa.randnum


class CriptFile:
    def __call__(self, data):
        def encrypt_rsa(*args, **kwargs):
            (pubkey, privkey) = rsa.newkeys(2048)
            crypto = rsa.encrypt(data(*args, **kwargs), pubkey)
            print(crypto)
        return encrypt_rsa

    @staticmethod
    def doc(address):
        with open(address) as fp:
            document = fp.read()
            for element in document[::]:
                element = str(element)
            document = str.encode(document)
        return document

class WriteToNewTxt:
    def __init__(self, directory_address, data_encrypt_text):
        self.directory_address = directory_address
        self.data_encrypt_text = data_encrypt_text

    def Create_txt_encript(self, directory_address):
        system('cd ' + directory_address)
        system('NUL> encript.txt')

    def Write_in_txt(self, data_encrypt_text):
        with open('encript.txt', 'w') as output:
            output.write(data_encrypt_text)
            output.close()

if __name__ == '__main__':
    system_check = platform
    if system_check == 'win32':
        def realization():
            print("---Enter the directory of file---")
            directory = str(input()) + '\\' + '\\'
            print("---Enter name of txt file---")
            name_file = str(input())
            address = directory + name_file
            try:
                print("---Result of RSA---")
                print(CriptFile.doc(address))
                to_str = str(CriptFile.doc(address))
                print(to_str)
                WriteToNewTxt(directory, to_str).Create_txt_encript(directory)
                WriteToNewTxt(directory, to_str).Write_in_txt(to_str)
            except OSError:
                print("Some problems...")
                exit()


        thread = threading.Thread(target=realization(), args=(1,))
        thread.start()
    else:
        print("---System is not win32---")
        exit()