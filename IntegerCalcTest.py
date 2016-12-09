import unittest
from ddt import ddt, file_data
from selenium import webdriver

# Wrapper
@ddt
class TestWrapper(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.eddyjones.com/test_stuff/advanced.html')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    @file_data('data/one_operation.json')
    def test_one_operation(self, test_data):

        print "test_data = {0}".format(test_data)

        self.arithmetic(self.driver, test_data)

    @file_data('data/data_two_operations.json')
    def test_two_operations(self, test_data):
        driver = webdriver.Chrome()
        driver.get('http://www.eddyjones.com/test_stuff/advanced.html')

        print "test_data = {0}".format(test_data)

        self.arithmetic(driver, test_data['operation1'])
        self.arithmetic(driver, test_data['operation2'])

    # [todo] Create additional test cases
    #1) Make method that inputs values then delete values.
    #2) Use method in point 1) input values then delete values then perform arithmetic on addition only
    #3) Use method in point 1) input values then delete values then perform arithmetic on subtraction only
    #a) input values then perform arithmetic on addition only then refresh and repeat
    #b) input values then perform arithmetic on subtraction only then refresh and repeat
    #c) as point a) and b) but with test_two_operations
    #[added] 4) input negative test case values: alpha, non-numeric, non-int
    #5) point 1) then input values into the result filed then perform addition
    #6) point 1) then input values into the result filed then perform subtraction
    #[added] 7) 64bit boundary test with 9223372036854775807
    #8) condense/orgainze inequality tests

    def arithmetic(self, driver, test_data):
        '''

        :param driver: selenium webdriver. Usage driver = webderiver.chrome()
        :param test_data: json object of the form
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
        '''

        # Data
        exp_sol = unicode(test_data['expected_sol'])

        # input values
        oper1 = driver.find_element_by_xpath('//*[@id="{oper1_ele}"]'.format(oper1_ele=test_data['operand1_ele']))
        oper1.send_keys("{op1_val}".format(op1_val=test_data['operand1_val']))
        oper2 = driver.find_element_by_xpath('//*[@id="{oper2_ele}"]'.format(oper2_ele=test_data['operand2_ele']))
        oper2.send_keys("{op2_val}".format(op2_val=test_data['operand2_val']))

        # Perform arithmetic
        driver.find_element_by_xpath('//*[@id="{oper_but}"]'.format(oper_but=test_data['operation_ele'])).click()

        # Results
        result = driver.find_element_by_xpath('//*[@id="{result}"]'.format(result=test_data['result'])).get_attribute('value')

        # Assert on errors
        self.assertEqual(exp_sol, result)


