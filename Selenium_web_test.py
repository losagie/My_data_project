from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#This is a sign up page funtionality test

class Trusted_web_test():
    def trusted_test(self):
        web_driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        web_driver.get('https://trustedinstitute.com')
        web_driver.maximize_window()
        web_driver.find_element(By.XPATH, "//a[normalize-space()='Get Started']").click()
        web_driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        web_driver.find_element(By.ID, "id_first_name").send_keys('lawrence')
        web_driver.find_element(By.ID, "id_last_name").send_keys('Gary')
        web_driver.find_element(By.NAME, "email").send_keys('mrechconstruct2@co.site')
        web_driver.find_element(By.XPATH, "//button[@id='register_submit']").click()
        winhand = web_driver.current_window_handle
        print(winhand)
        time.sleep(5)


Mytest = Trusted_web_test()
Mytest.trusted_test()

