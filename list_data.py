from extract_customer_data import ConfigurationParser
from ip_test import is_ip_address

cp = ConfigurationParser()
customer_names = cp.parseCustomerNames()

for name in customer_names:
    customer_vlan = cp.parseCustomerVlan(name)
    customer_ip = cp.parseCustomerIPAddress(customer_vlan)

    print(name + " - VLAN: " + str(customer_vlan) + " - IP Address: " + customer_ip + 
          " - IP Correto: " + is_ip_address.is_ip_address(customer_ip) + " - IP na Rede Correta: " + is_ip_address.is_ip_correct_network(customer_ip))


