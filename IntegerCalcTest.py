import unittest
from ddt import ddt, file_data
from selenium import webdriver

# Wrapper
@ddt
class TestWrapper(unittest.TestCase):
   @file_data('test_cases.json')
   def test_case(self, test_data):
       driver = webdriver.Chrome()
       driver.get('http://www.eddyjones.com/test_stuff/advanced.html')

       print "test_data = {0}".format(test_data)

       # Data
       operand1_ele = test_data['operand1_ele']
       operand2_ele = test_data['operand2_ele']
       result = test_data['result']
       operation_ele = test_data['operation_ele']
       operand1_val = test_data['operand1_val']
       operand2_val = test_data['operand2_val']
       expected_sol = test_data['expected_sol']
       exp_sol = unicode(expected_sol)

       # Test
       oper1 = driver.find_element_by_xpath('//*[@id="{oper1_ele}"]'.format(oper1_ele=operand1_ele))
       oper1.send_keys("{op1_val}".format(op1_val = operand1_val))
       oper2 = driver.find_element_by_xpath('//*[@id="{oper2_ele}"]'.format(oper2_ele=operand2_ele))
       oper2.send_keys("{op2_val}".format(op2_val = operand2_val))

       driver.find_element_by_xpath('//*[@id="{oper_but}"]'.format(oper_but=operation_ele)).click()
       result = driver.find_element_by_xpath('//*[@id="{result}"]'.format(result=result)).get_attribute('value')

       assert(exp_sol == result)

       driver.close()


