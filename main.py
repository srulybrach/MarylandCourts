from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://casesearch.courts.state.md.us/casesearch/inquiry-index.jsp"
driver.get(url)

element = driver.find_element(By.ID, "btnDisclaimerAgree")
driver.execute_script("arguments[0].removeAttribute('data-callback')", element)
driver.execute_script("arguments[0].removeAttribute('data-sitekey')", element)
driver.execute_script("arguments[0].removeAttribute('data-action')", element)

driver.execute_script("arguments[0].setAttribute('class','button')", element)

driver.find_element(By.NAME, "disclaimer").click()
driver.find_element(By.ID, "btnDisclaimerAgree").click()

