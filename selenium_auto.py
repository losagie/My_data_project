from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

web_driver = webdriver.Chrome( service=Service(executable_path=ChromeDriverManager().install()))
web_driver.get("https://trustedinstitute.com")
web_driver.maximize_window()
time.sleep(5)
print(web_driver.title)
web_driver.quit()

