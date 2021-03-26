import scapy.all as sp



def arp(ip="192.168.0.105"):
    arp_packet=sp.ARP(pdst=ip)
    brodcast=sp.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_and_brodcast=brodcast/arp_packet
    answer=sp.srp(arp_and_brodcast,verbose=False,timeout=1)[0]
    #return answer[0][1].hwsrc

arp()
