import os
import sys
import urllib 
import re



class func(object):
    


    
    def getMacAddress(self, type):
        """ 
            This has been added by John Roach.
            works in both windows and linux
            Why Windows? Because I can!!!
        """
        
        if sys.platform == 'win32':
            for line in os.popen("ipconfig /all"):
                if line.lstrip().startswith('Physical Address'):
                    mac = line.split(':')[1].strip().replace('-',':')
                    break
        else:
            for line in os.popen("/sbin/ifconfig"):
                if line.find(type) > -1:
                    mac = line.split()[4]
                    break
        return mac 
    
    def getIPAddress(self):
        """
           This program gets your external ip
           from whatismyip.com
           this program must be called every
           5 minutes not more or else you must
           have your own server.
        """
        site = urllib.urlopen("http://www.whatismyip.com/automation/n09230945.asp").read()
        grab = re.findall('\d{2,3}.\d{2,3}.\d{2,3}.\d{2,3}',site)
        address = grab[0]
        return address

        