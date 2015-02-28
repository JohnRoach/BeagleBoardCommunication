"""
Simple chat client for the chat server. Defines
a simple protocol to be used with chatserver.

"""

import socket
import sys
import select
from communication import send, receive
import functions
import string
import hashlib
import ssh
import os


BUFSIZ = 1024

def contains(theString, theQueryValue):
  return theString.find(theQueryValue) > -1

def md5(fileName, excludeLine="", includeLine=""):
        """Compute md5 hash of the specified file"""
        m = hashlib.md5()
        try:
            fd = open(fileName,"rb")
        except IOError:
            print ("Unable to open the file in readmode:"+filename)
            return
        content = fd.readlines()
        fd.close()
        for eachLine in content:
            if excludeLine and eachLine.startswith(excludeLine):
                continue
            m.update(eachLine)
        m.update(includeLine)
        return m.hexdigest()        


class ChatClient(object):
    """ A simple command line chat client using select """

    def __init__(self, name, host='127.0.0.1', port=3491):
        self.name = name
        # Quit flag
        self.flag = False
        self.port = int(port)
        self.host = host
        # Initial prompt
        self.prompt='[' + '@'.join((name, socket.gethostname().split('.')[0])) + ']> '
        # Connect to server at port
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, self.port))
            print ('Connected to chat server@%d' % self.port)
            # Send my name...
            send(self.sock,'NAME: ' + self.name) 
            data = receive(self.sock)
            # Contains client address, set it
            addr = data.split('CLIENT: ')[1]
            self.prompt = '[' + '@'.join((self.name, addr)) + ']> '
        except (socket.error):
            print ('Could not connect to chat server @%d' % self.port)
            sys.exit(1)

    def cmdloop(self):

        while not self.flag:
            try:
                sys.stdout.write(self.prompt)
                sys.stdout.flush()

                # Wait for input from stdin & socket
                inputready, outputready,exceptrdy = select.select([0, self.sock], [],[])
                
                for i in inputready:
                    if i == 0:
                        data = sys.stdin.readline().strip()
                        if data: send(self.sock, data)
                    elif i == self.sock:
                        data = receive(self.sock)

                        if not data:
                            print ('Shutting down.')
                            self.flag = True
                            break
                        else:
                            token = string.split(data, '@')
                            if token[0].startswith('\n#[SERVER'):
                                if token[2] == mac :
                                    #token[3] is the data sent from the server
                                    sys.stdout.write('Server wants : '+token[3]+ '\n')
                                    sys.stdout.flush()
                                    if token[3]=="need_update" :
                                        file_name='test_data.csv' #this is actually very wrong to do but 26th of April is just too soon to finish project!
                                        md_code=md5(file_name)
                                        data='@'+'sending_update'+'@'+file_name+'@'+str(md_code)
                                        send(self.sock, data)
                                        s = ssh.Connection(host = '192.168.1.38', username = 'john', password = 'rabbit&foam')
                                        s.put(file_name, '/var/www/html/IPBox/functions/user_func/userfolders/john/'+file_name)
                                        s.close()         
                                        data='@file_sent|'+file_name+'|'+str(md_code)
                                        send(self.sock, data)
                                    if token[3].startswith("get_file"):
                                        sub_token = string.split(token[3],'|')
                                        s = ssh.Connection(host = '192.168.1.38', username = 'john', password = 'rabbit&foam')
                                        s.get(sub_token[1],'/home/root/'+sub_token[2] )
                                        s.close()
                                        data='@got_file'
                                        send(self.sock, data)
                                        
                                        
            
                                        
                                        
                                        
                                        
                                        
                            
            except KeyboardInterrupt:
                print ('Interrupted.')
                self.sock.close()
                break
            
   
if __name__ == "__main__":
    import sys
    
    
    
    """ don't really need it now however will leave it just in case..
    if len(sys.argv)<3:
        sys.exit('Usage: %s chatid host portno' % sys.argv[0])
    """    
    f = functions.func()
    """          Get MAC           """
    """Ethernet = eth  Wi-Fi = wlan"""
    """  Chose Ethernet for now    """
    #mac = f.getMacAddress(type = 'wlan') 
    #commented since we are currently debugging 
    mac='00:A1:B0:B0:2C:BC';
    """ Server info. May create config file for this """
    
    #host = '193.140.221.90'
    host = '192.168.1.38'
    port = '3491'
    
      
    client = ChatClient( '@'+mac,host, int(port))
    client.cmdloop()
