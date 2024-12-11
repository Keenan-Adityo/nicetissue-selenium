from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

@pytest.fixture(scope="function")
def driver():
    service = Service()  
    driver = webdriver.Chrome(service=service)
    yield driver  
    driver.quit()  

def testcase_05(driver):
    # setup
    driver.get("https://www.nicetissue.id")  
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fa-times"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "MASUK/DAFTAR"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    ).send_keys("salsabillaputerisandiwardana@gmail.com")  

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    ).send_keys("Salsa110099") 

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-primary"))
    ).click()
    time.sleep(3)
    #TC-08
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "REDEEM"))
    ).click()
    # time.sleep(3)
    WebDriverWait(driver, 10).until(
        lambda d: d.current_url == "https://www.nicetissue.id/profile/redeem"
    )
    assert driver.current_url == "https://www.nicetissue.id/profile/redeem", "Not redirected to redeem page"
    time.sleep(3)
    