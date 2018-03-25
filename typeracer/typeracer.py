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
	return driver

def type(driver):
	driver.get("http://play.typeracer.com/")
	time.sleep(3)

	#bypass the first screen
	try:
		driver.find_element_by_xpath("//table[@class='mainMenuItemText']/tbody/tr[1]/td[1]/a[@class='gwt-Anchor']").click()
	except:
		print("error")

	#if you get traceback error, try increasing this time
	time.sleep(15)


	try:
		input_box = driver.find_element_by_xpath("//td/input[@type='text']")
	except:
		print("no input box found")

	temp = 0
	text_final = []

	try:
		words = driver.find_element_by_xpath("//table[@class='inputPanel']/tbody/tr/td/table/tbody/tr/td/div/div/span[3]")
	except:
		temp = 1

	try:
		words = driver.find_element_by_xpath("//table[@class='inputPanel']/tbody/tr/td/table/tbody/tr/td/div/div/span[1]")
		print(words.text)
		if temp == 1:
			text_final.append(words.text)
		else:
			temp_text = words.text
	except:
		print("error in first key")
				
	try:
		words = driver.find_element_by_xpath("//table[@class='inputPanel']/tbody/tr/td/table/tbody/tr/td/div/div/span[2]")
		print(words.text)
		if temp ==1:
			text = words.text.split()
			text_final.extend(text)
		else:
			temp_text += words.text
			text_final.append(temp_text)
	except:
		print("error in second key")

	try:
		words = driver.find_element_by_xpath("//table[@class='inputPanel']/tbody/tr/td/table/tbody/tr/td/div/div/span[3]")
		print(words.text)
		text = words.text.split()
		text_final.extend(text)
	except:
		print("remaining words not found")
	
	print("final array is: ")
	print(text_final)

	input_box.send_keys(text_final[0])
	if(text_final[1]==',' or text_final[1]=='.'):
		input_box.send_keys(text_final[1])
		input_box.send_keys(" ")
		try:
			for i in range(2,len(text_final)):
				time.sleep(0.1)
				input_box.send_keys(text_final[i])
				input_box.send_keys(" ")
				time.sleep(0.1)
		except:
			print("error in printing")
	else:
		input_box.send_keys(" ")
		try:
			for i in range(1,len(text_final)):
				time.sleep(0.1)
				input_box.send_keys(text_final[i])
				input_box.send_keys(" ")
				time.sleep(0.1)
		except:
			print("error in printing")
				

if __name__ == "__main__":
    driver = init_driver()
    type(driver)