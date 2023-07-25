import unittest
from extract_customer_data import ConfigurationParser

class TestParse(unittest.TestCase):
    def test_parse_cust_name(self):
        cp = ConfigurationParser()
        expected_names = ['CUSTOMER_A', 'CUSTOMER_B']
        parsed_names = cp.parseCustomerNames()
        self.assertEqual(list, type(parsed_names))
        self.assertEqual(expected_names, parsed_names)

    def test_parse_cust_vlan(self):
        cp = ConfigurationParser()
        customer_name = "CUSTOMER_A"
        expect_vlan = 100
        parsed_vlan = cp.parseCustomerVlan(customer_name)
        self.assertEqual(expect_vlan, parsed_vlan)

        

