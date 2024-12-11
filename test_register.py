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

def testcase_02(driver):
    # setup
    driver.get("https://www.nicetissue.id")  
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fa-times"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "MASUK/DAFTAR"))
    ).click()

    # TC-02
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "DAFTAR"))
    ).click()

    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "firstname"))
    ).send_keys("Salsabilla")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "lastname"))
    ).send_keys("Putri")    

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@name='email'])[2]"))
    ).send_keys("salsabillaputerisandiwardana")


    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@name='password'])[2]"))
    ).send_keys("Salsa11009")  

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password_confirmation"))
    ).send_keys("Salsa11009")  
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-phone"))
    ).click()

    time.sleep(3)

    firstnameField = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "firstname"))
    )
    assert firstnameField is not None, "Should Fail to register"
    
    