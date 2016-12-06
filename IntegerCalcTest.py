from selenium import webdriver


driver = webdriver.Chrome()


driver.get('http://www.eddyjones.com/test_stuff/advanced.html')


# Inputs
test_cases = {
   "operand1_ele" : 'addition_number_1',
   "operand2_ele" : 'addition_number_2',
   "operation_ele" : 'addition_action_1',
   "operand1_val" : 10,
   "operand2_val" : 7,
   "expected_sol" : 17
}
# Wrapper
# Data
operand1_ele = test_cases['operand1_ele']
operand2_ele = test_cases['operand2_ele']
operation_ele = test_cases['operation_ele']
operand1_val = test_cases['operand1_val']
operand2_val = test_cases['operand2_val']
expected_sol = test_cases['expected_sol']
exp_sol = unicode(expected_sol)


# Test
oper1 = driver.find_element_by_xpath('//*[@id="{oper1_ele}"]'.format(oper1_ele=operand1_ele))
oper1.send_keys("{op1_val}".format(op1_val = operand1_val))
oper2 = driver.find_element_by_xpath('//*[@id="{oper2_ele}"]'.format(oper2_ele=operand2_ele))
oper2.send_keys("{op2_val}".format(op2_val = operand2_val))


driver.find_element_by_xpath('//*[@id="{oper_but}"]'.format(oper_but=operation_ele)).click()
result = driver.find_element_by_xpath('//*[@id="addition_sum"]').get_attribute('value')


assert(exp_sol == result)


driver.close()


