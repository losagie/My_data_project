from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class TrustedWebTest():
    def Test_by_Tag(self):
        web_driver = webdriver.Chrome(service=Service(executable_path=(ChromeDriverManager().install())))
        web_driver.get("https://trustedinstitute.com")
        web_driver.maximize_window()
        tagnames =  web_driver.find_elements(By.TAG_NAME, "a")
        print(tagnames)
        print(len(tagnames))
        for i in tagnames:
            print(i.text)
        time.sleep(5)
        web_driver.quit()


DemoTag = TrustedWebTest()
DemoTag.Test_by_Tag()


