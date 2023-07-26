from extract_customer_data import ConfigurationParser

cp = ConfigurationParser()
customer_names = cp.parseCustomerNames()

for name in customer_names:
    print(name)
    customer_vlan = cp.parseCustomerVlan(name)
    print(customer_vlan)
