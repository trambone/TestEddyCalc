from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://www.eddyjones.com/test_stuff/advanced.html')

exp_sol = unicode(17)

# Test
oper1 = driver.find_element_by_xpath('//*[@id="{oper1_ele}"]'.format(oper1_ele="addition_number_1"))
oper1.send_keys("{op1_val}".format(op1_val = 10))
oper2 = driver.find_element_by_xpath('//*[@id="{oper2_ele}"]'.format(oper2_ele="addition_number_2"))
oper2.send_keys("{op2_val}".format(op2_val = 7))

driver.find_element_by_xpath('//*[@id="{oper_but}"]'.format(oper_but="addition_action_1")).click()
result = driver.find_element_by_xpath('//*[@id="addition_sum"]').get_attribute('value')

assert(exp_sol == result)

driver.close()