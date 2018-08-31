import nmap
from colorama import Fore

nm = nmap.PortScanner()

def scan(iphost):
   for listport in range (21,443):
      scan = nm.scan(iphost,str(listport))
      for protocol in nm[iphost].all_protocols():
          idport = nm[iphost][protocol].keys()
          for port in idport:
              if nm[iphost][protocol][listport]['state'] == 'open' or nm[iphost][protocol][listport]['state'] == 'filtered':
                 print(Fore.GREEN)   
                 print ('Port: %d'% listport, 'State: %s' % nm[iphost][protocol][listport]['state'])
              else:
                 print (Fore.RED)
                 print ('Port: %d'% listport, 'State:closed' )


if  __name__ == "__main__":
    ipscan = raw_input ("Ip to scan: ")
    analyz = scan(ipscan)
    

