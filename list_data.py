from extract_customer_data import ConfigurationParser

cp = ConfigurationParser()
customer_names = cp.parseCustomerNames()

for name in customer_names:
    customer_vlan = cp.parseCustomerVlan(name)
    customer_ip = cp.parseCustomerIPAddress(customer_vlan)
    print(name + " - VLAN: " + str(customer_vlan) + " - IP Address: " + customer_ip)


