from sys import exit
from pynput import keyboard
from time import sleep
from threading import Thread, ThreadError

vec_str = []
file = open("test.txt", "w")

def to_tread(func):
    def wrapper(*args):
        try:
            Thread(target=func, args = (*args, )).run()
        except ThreadError:
            exit(1)
    return wrapper


@to_tread
def input_to_file(vec_str: list, file) -> None:
    for line in vec_str:
        file.write(f"{line}\n")


@to_tread
def main() -> None:
    with keyboard.Events() as events:
        for event in events:
            tmp = event.key
            vec_str.append(str(tmp))
            if tmp is None:
                sleep(0.1)
            print(f"you enter > {tmp}")
            input_to_file(vec_str, file)


if __name__ == '__main__':
    try:
        main()
    except:
        exit(0)
