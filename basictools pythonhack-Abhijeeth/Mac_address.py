import subprocess
import optparse

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="interface please")
    parser.add_option("-m","--mac",dest="mac",help="mac Please")
    (options,arguments)=parser.parse_args()
    if not options.interface:
        print("[-] Inter face nokkara kuyya")
    elif not options.mac:
        print("[-]Mac nokkara kuyya")
    return options

def change_mac(interface,mac):
    subprocess.call(["inconfig",interface,"down"])
    subprocess.call(["ifconfog",inteface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])
    print("DONE!!!")
    
    
#proc = subprocess.check_output("ipconfig" ).decode('utf-8')
#print (proc)
options=get_arguments()
change_mac(options.interface,options.mac)
#00:0c:29:21:fa:bd
