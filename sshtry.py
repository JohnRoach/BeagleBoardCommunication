"""This program will work on BeagleBoard to send configurations """
"""to the server. The configurations that will be sent will be  """
"""                                                             """
"""   * The MAC address of the                                  """
"""   * The IP of the BeagleBoard                               """
"""   * The port used by the BeagleBoard                        """
"""                                                             """
""" The program will start at power-up of the beagle board      """
"""                                                             """
""" Dependencies : Python, ssh.py, functions.py paramiko        """
"""                                                             """
""" *Paramiko can be downloaded from                            """
"""  http://www.lag.net/paramiko/                               """
"""                                                             """
""" Questions? Comments? : johnroach.info                       """

import ssh
import functions


""" This connection is basicly to the server                    """
""" For testing this is basicly my desktop-computer running     """
""" A special user has been created for this project with       """
""" limited privilages this user is johnroach                   """
""" The IP of the server is 192.168.1.33                        """
s = ssh.Connection(host = '193.140.221.89', username = 'blackboxuser', password = 'fourty@ankara')

""" Calling the functions functions :) """
f = functions.func()

"""          Get MAC           """
"""Ethernet = eth  Wi-Fi = wlan"""
"""  Chose Ethernet for now    """
mac = f.getMacAddress(type = 'wlan')

"""          Get IP         """
ip = f.getIPAddress()


try :
    s.execute('python /home/blackboxuser/getipmac.py '+mac+' '+ip)

except :
    print ('Error!')
    
s.close()
