from scapy.all import *
import optparse


def arp(ip):
    parser=optparse.OptionParser()
    #parser.add_option("-ip","--ip",dest="ip",help="subnet please")
    #(options,arguments)=praser.prase_args()
    #if not options.ip:
     #   print("[-] Inter face nokkara kuyya")
    #else:
     #   print(options.ip)
     
    #arp_packet=arping(ip,verbose="less")
    arp_packet=ARP(pdst=ip)
    brodcast=Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_and_brodcast=brodcast/arp_packet
    #print(arp_and_brodcast.summary())
    answer=srp(arp_and_brodcast,verbose=False,timeout=1)[0]
    #print(answer.summary())
    #print(unanswer.summary)
    print("IP\t\t\tMAC\n====================================")
    for i in answer:
    	#print(i[1].show())
    	print(i[1].psrc+"     |    "+i[1].hwsrc)
    #print(arp_packet.summary())
    #ls(Ether)
    #print(arp_packet.show())   
arp("192.168.0.1/24")

# Currently scanning: 192.168.128.0/16   |   Screen View: Unique Hosts              
                                                                                   
 #36 Captured ARP Req/Rep packets, from 3 hosts.   Total size: 2160                 
# _____________________________________________________________________________
 #  IP            At MAC Address     Count     Len  MAC Vendor / Hostname      
 #-----------------------------------------------------------------------------
 #192.168.0.104   80:91:33:94:37:9f      9     540  AzureWave Technology Inc.       
 #192.168.0.1     50:d4:f7:ef:51:16     26    1560  TP-LINK TECHNOLOGIES CO.,LTD.   
 #192.168.0.100   8c:57:9b:fe:44:95      1      60  Wistron Neweb Corporation       

