from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome()
#write your login page adress
driver.get("http://10.6.24.148:880/2/login.html?ga_ssid=PB-GUEST&ga_ap_mac=00-08-56-BA-1F-2E&ga_nas_id=PB-GAMA-905&ga_srsr=10.16.24.148&ga_cmac=E8-2A-33-F3-2E-B5&ga_Qv=eERADR87HBgAGDEEVgQAGw4UWRUCACYVMgFPQC9ZKlZfVidGXIuHtZSyRjLfBhFMUMww.")
					#Update 1 =) Copy the link of loging screen
time.sleep(.8)

username = driver.find_element_by_name("ga_user")
password = driver.find_element_by_name("ga_pass")
button = driver.find_element_by_xpath('//*[@id="LoginPage"]/input[3]')

username.send_keys("your username")			#Update 2
password.send_keys("your password")			#Update 3

button.click()
time.sleep(.8)

driver.close()
