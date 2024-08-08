
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
import logging as log
import json

class Login():
    
    def __init__ (self):
        
        self.log = log
        log.basicConfig(filename="loginpage_test.log", level=log.DEBUG)
        self.driver = webdriver.Chrome()
        self.baseUrl = "http://127.0.0.1:5500/index.html"
        self.userNameId = "txt_inp_username"
        self.passwordId = "txt_inp_password"
        self.submitId = "btn_submit"
        self.messageBoxId = "p_message"

        
    def login_valid_credentials(self):
        try:
            self.driver.get(self.baseUrl)
            self.driver.maximize_window()
            with open('login_testcases_result.json', 'r') as file:
                data = json.load(file)
            file.close()
            username = self.driver.find_element(By.ID,self.userNameId)
            if(username):
                self.log.info("Found UserName")
                username.send_keys("admin")
            else:
                self.log.error("UserName not found")
            self.driver.implicitly_wait(2)
            
            password = self.driver.find_element(By.ID,self.passwordId)
            if(password):
                self.log.info("Found password")
                password.send_keys("password")
            else:
                self.log.error("password not found")
                
            self.driver.implicitly_wait(2)            
            submit = self.driver.find_element(By.ID,self.submitId)
            if(submit):
                self.log.info("Found submit button")
                submit.click()
                self.driver.implicitly_wait(50)
            else:
                self.log.error("submit button not found")
            
            message = self.driver.find_element(By.ID,self.messageBoxId)
            if(message):
                self.log.info("Found message box")
                messageText = message.text
            else:
                self.log.error("message box not found")
            if messageText == "Login successful!":
                data['testcase_1']['test_case_actual_result'] = "login successful!"
                data['testcase_1']['end_result'] = "pass"
            else:
                data['testcase_1']['test_case_actual_result'] = "login successful! message was not displayed"
                data['testcase_1']['end_result'] = "fail" 
            destinationFileName = "testcase_1.png"
            self.driver.save_screenshot(destinationFileName)
            with open('login_testcases_result.json', 'w') as file:
                json.dump(data, file, indent=4)
                self.log.info("result json updated")
        except():
            print("error occured in login_valid_credentials")
            
    def login_invalid_credentials(self):
        try:
            self.driver.get(self.baseUrl)
            self.driver.maximize_window()
            with open('login_testcases_result.json', 'r') as file:
                data = json.load(file)
            file.close()            
            username = self.driver.find_element(By.ID,self.userNameId)
            if(username):
                self.log.info("Found UserName")
                username.send_keys("admin123")
            else:
                self.log.error("UserName not found")
            self.driver.implicitly_wait(2)
            
            password = self.driver.find_element(By.ID,self.passwordId)
            if(password):
                self.log.info("Found password")
                password.send_keys("password123")
            else:
                self.log.error("password not found")
                
            self.driver.implicitly_wait(2)            
            submit = self.driver.find_element(By.ID,self.submitId)
            if(submit):
                self.log.info("Found submit button")
                submit.click()
                self.driver.implicitly_wait(50)
            else:
                self.log.error("submit button not found")
            
            message = self.driver.find_element(By.ID,self.messageBoxId)
            if(message):
                self.log.info("Found message box")
                messageText = message.text
            else:
                self.log.error("message box not found")
            if messageText == "Invalid username or password.":
                self.log.info("testcase_2 passed")
                data['testcase_2']['test_case_actual_result'] = "Invalid username or password."
                data['testcase_2']['end_result'] = "pass"
            else:
                self.log.info("testcase_2 failed")
                data['testcase_2']['test_case_actual_result'] = "Invalid username or password. message not displayed"
                data['testcase_2']['end_result'] = "fail" 
            destinationFileName = "testcase_2.png"
            self.driver.save_screenshot(destinationFileName)
            with open('login_testcases_result.json', 'w') as file:
                json.dump(data, file, indent=4)
                self.log.info("result json updated")
        except():
            print("error occured in login_invalid_credentials")
            
loginObj = Login()
loginObj.login_valid_credentials()
loginObj.login_invalid_credentials()

        
    
    
        
        