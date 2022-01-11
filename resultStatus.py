from selenium import webdriver
from selenium.webdriver.support.ui import Select

mainDriver = webdriver.Chrome(executable_path='chromedriver_win32\chromedriver.exe')
mainDriver.get('https://result.ganpatuniversity.ac.in/')
mainDriver.find_element_by_xpath("//select[@name='ddlInst']/option[text()='16 - ICT']").click()
mainDriver.find_element_by_xpath("//select[@name='ddlDegree']/option[text()='B.TECH-CSE(CS)']").click()
mainDriver.find_element_by_xpath("//select[@name='ddlSem']/option[text()='V']").click()
examsList = Select(mainDriver.find_element_by_xpath("//select[@name='ddlScheduleExam']")).options
for i in examsList:
    print(i.text)
mainDriver.close()
if len(examsList) > 3:
    print('Result for SEM V has been declared.')
else:
    print('Result has not yet been declared.')
