# IOS XE 
#Netconf 
#Configure loopback interface and get reply

#!/usr/bin/env python

from lxml import etree
from ncclient import manager

if __name__ == "__main__":

    with manager.connect(host='172.16.30.23', 
	                port=830, 
					username='admin', 
					password='P@ssw0rd',
	                timeout=90,
					hostkey_verify=False, 
					device_params={'name': 'csr'}) as device:


        nc_filter = """
                <config>
                <native xmlns="http://cisco.com/ns/yang/ned/ios">
                 <interface>
                  <Loopback>
                   <name>200</name>
                   <ip>
                    <address>
                        <primary>
                            <address>10.200.20.1</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                        <secondary>
                            <address>9.9.9.9</address>
                            <mask>255.255.255.0</mask>
                            <secondary/>
                        </secondary>
                        <secondary>
                            <address>11.11.11.1</address>
                            <mask>255.255.255.0</mask>
                            <secondary/>
                        </secondary>
                    </address>
                   </ip>
                  </Loopback>
                 </interface>
                </native>
                </config>
        """

        nc_reply = device.edit_config(target='running', config=nc_filter)

        get_filter = """
            <native xmlns="http://cisco.com/ns/yang/ned/ios">
              <interface>
                <Loopback>
                  <name>200</name>
                </Loopback>
              </interface>
            </native>
        """
        nc_get_reply = device.get(('subtree', get_filter))
        print etree.tostring(nc_get_reply.data_ele, pretty_print=True)