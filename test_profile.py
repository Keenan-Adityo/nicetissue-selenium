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

def testcase_03_05_06(driver):
    # setup
    driver.get("https://www.nicetissue.id")  
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fa-times"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "MASUK/DAFTAR"))
    ).click()

    #TC-04
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    ).send_keys("salsabillaputerisandiwardana@gmail.com")  

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    ).send_keys("Salsa110099wrong") 

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-primary"))
    ).click()

    time.sleep(1)
    errorMessage = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "error"))
    )
    assert errorMessage is not None, "Should Fail to login"

    # TC-03
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    ).clear()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    ).send_keys("Salsa110099") 

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-primary"))
    ).click()
    time.sleep(3)
    
    WebDriverWait(driver, 10).until(
        lambda d: d.current_url == "https://www.nicetissue.id/profile"
    )
    assert driver.current_url == "https://www.nicetissue.id/profile", "Not redirected to profile page"

    #TC-03
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "firstname"))
    ).clear()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "lastname"))
    ).clear()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "address"))
    ).clear()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "subdistrict"))
    ).clear()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "postal_code"))
    ).clear()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-save"))
    ).click()
    time.sleep(3)
    

    alert = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
    )
    assert alert is not None, "Should Fail to save"

    #TC-04
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "firstname"))
    ).send_keys("Salsabilla")  

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "lastname"))
    ).send_keys("Puteris")  

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "address"))
    ).send_keys("Jl. Kenangan")  

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "subdistrict"))
    ).send_keys("Blater")  

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "postal_code"))
    ).send_keys("76823")  

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-save"))
    ).click()
    time.sleep(3)
    

    alert = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))
    )
    assert alert is not None, "Should Success to save"