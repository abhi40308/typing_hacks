import os
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def init_driver():
	chromedriver = "/Users/*username*/Downloads/chromedriver"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)
	# driver.wait = WebDriverWait(driver, 5)
	return driver

def type(driver):
	driver.get("https://10fastfingers.com/typing-test/english")
	time.sleep(5)
	input_box = driver.find_element_by_id('inputfield')
	i=0
	while True:
		word = driver.find_element_by_xpath("//span[@wordnr='" + str(i) + "']")
		input_box.send_keys(word.text)
		input_box.send_keys(" ")
		i+=1

if __name__ == "__main__":
    driver = init_driver()
    type(driver)