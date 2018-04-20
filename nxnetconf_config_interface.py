# Config interface using ncclient
# Nexus 

#!/usr/bin/env python

from ncclient import manager

hostname = '172.16.30.24'
username = 'admin'
password = 'P@ssword'

if __name__ == '__main__':

    with manager.connect(host='172.16.30.24', 
                         port=22, 
                         username='admin', 
                         password='P@ssw0rd',
                         hostkey_verify=False, 
                         device_params={'name': 'nexus'}, 
                         timeout=90) as device:

        commands = ['config t', 'interface e1/1', 'description TEST']
        nc_config_reply = device.exec_command(commands)
        print nc_config_reply.xml
		
