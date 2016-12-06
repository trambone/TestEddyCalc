import unittest
from ddt import ddt, file_data
from selenium import webdriver

# Wrapper
@ddt
class TestWrapper(unittest.TestCase):
    @file_data('data_one_operation.json')
    def test_one_operation(self, test_data):
        driver = webdriver.Chrome()
        driver.get('http://www.eddyjones.com/test_stuff/advanced.html')

        print "test_data = {0}".format(test_data)

        self.arithmetic(driver, test_data)

        driver.close()

    @file_data('data_two_operations.json')
    def test_two_operations(self, test_data):
        driver = webdriver.Chrome()
        driver.get('http://www.eddyjones.com/test_stuff/advanced.html')

        print "test_data = {0}".format(test_data)

        self.arithmetic(driver, test_data['operation1'])
        self.arithmetic(driver, test_data['operation2'])

        driver.close()

    def arithmetic(self, driver, test_data):
        '''

        :param driver: selenium webdriver. Usage driver = webderiver.chrome()
        :param test_data: json object.
        test_data = {
             u'operand2_val': 7,
             u'operation_ele': u'addition_action_1',
             u'result': u'addition_sum',
             u'operand2_ele':
             u'addition_number_2',
             u'operand1_ele':
             u'addition_number_1',
             u'operand1_val': 10,
             u'expected_sol': 17}
        :return:
        '''

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
        # Enter values
        oper1 = driver.find_element_by_xpath('//*[@id="{oper1_ele}"]'.format(oper1_ele=operand1_ele))
        oper1.send_keys("{op1_val}".format(op1_val=operand1_val))
        oper2 = driver.find_element_by_xpath('//*[@id="{oper2_ele}"]'.format(oper2_ele=operand2_ele))
        oper2.send_keys("{op2_val}".format(op2_val=operand2_val))

        # Perform arithmetic
        driver.find_element_by_xpath('//*[@id="{oper_but}"]'.format(oper_but=operation_ele)).click()

        # Results
        result = driver.find_element_by_xpath('//*[@id="{result}"]'.format(result=result)).get_attribute('value')

        # Assert on errors
        self.assertEqual(exp_sol, result)


