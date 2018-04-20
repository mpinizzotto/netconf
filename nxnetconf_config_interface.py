# Config interface using ncclient
#

#!/usr/bin/env python

from ncclient import manager

hostname = '172.16.30.23'
username = 'admin'
password = 'P@ssword'

if __name__ == '__main__':

    with manager.connect(host='172.16.30.23', 
                         port=830, 
                         username='admin', 
                         password='P@ssw0rd',
                         hostkey_verify=False, 
                         device_params={'name': 'csr'}, 
                         timeout=90) as device:

        commands = ['config t', 'interface GigabitEthernet1/2', 'ip address 10.1.1.1 255.255.255.0','description CONNECTION TO RTR-02']
        nc_config_reply = device.exec_command(commands)
        print nc_config_reply.xml
		
