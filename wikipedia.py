from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Python27\Scripts\chromedriver.exe")
driver.get('https://en.wikipedia.org')


random_link = driver.find_element_by_id('n-randompage')
random_link.click()
time.sleep(5)

print(driver.title)

driver.quit()