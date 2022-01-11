from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image
import os


def generateImage(filename):
    driver = webdriver.Chrome()
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=chrome_options)
    url = "https://result.ganpatuniversity.ac.in/"

    driver.get(url)

    # institute
    driver.find_element_by_name('ddlInst').click()
    driver.find_element_by_xpath(
        '/html/body/form/div[3]/table[2]/tbody/tr[1]/td[2]/select/option[18]').click()

    # Degree
    driver.find_element_by_name('ddlDegree').click()
    driver.find_element_by_xpath(
        '/html/body/form/div[3]/table[2]/tbody/tr[2]/td[2]/select/option[3]').click()

    # Sem
    driver.find_element_by_name('ddlSem').click()
    driver.find_element_by_xpath(
        '/html/body/form/div[3]/table[2]/tbody/tr[3]/td[2]/select/option[6]').click()
    # Exam
    driver.find_element_by_name('ddlScheduleExam').click()
    ssName = filename
    ss = driver.save_screenshot(ssName)


def compare():
    # Find and print the diff:
    os.system('cmd /c "certutil -hashfile mScreenshot.png SHA256> oldHash.txt"')
    mFile = open("oldHash.txt")
    hashVal = mFile.readlines()
    os.system('cmd /c "certutil -hashfile nScreenshot.png SHA256> newHash.txt"')
    newFile = open("newHash.txt")
    newHashVal = newFile.readlines()
    if hashVal[1] != newHashVal[1]:
        # remove mScreenShot and rename nScreenShot.png as mScreenshot.png
        print("Some Update found")
        os.remove('mScreenShot.png')
        os.rename('nScreenShot.png', 'mScreenShot.png')
        # sendMail()
    else:
        print("No changes found.\nDeleting nScreenShot.png")
        os.remove('nScreenShot.png')


# driver code
# when mScreenshot is already present in current dir
if os.path.exists("mScreenShot.png"):
    # Append-adds at last
    print("mScreenShot file is existing")
    # Generating Current Screenshot
    generateImage('nScreenShot.png')
    print("Stored in nScreenshot.png FILE")
    compare()
else:  # when the script is running for very first time
    print("FILE: mScreenShot.png doesn't exist")
    # Generating Current Screenshot
    generateImage('mScreenShot.png')
    print("Stored in mScreenShot.png FILE")
