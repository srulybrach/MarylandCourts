from selenium import webdriver
from datetime import date
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://casesearch.courts.state.md.us/casesearch/inquiry-index.jsp"
driver.get(url)
driver.find_element(By.NAME, "disclaimer").click()
driver.find_element(By.ID, "btnDisclaimerAgree").click()