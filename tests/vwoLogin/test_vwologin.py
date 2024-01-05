'''
Selenium handles only automation part:
Selenium is not a testing framework and it can automate only browsers.

Test case Steps:
Open the Browser
Navigate to URL
Find the Email Web-element & enter  email id= "abc@gmail.com"
Find the Password input box & enter the password=123
Click on Sign-in Button
'''


'''
Verification part/Assertion part is taken care by Pytest testing framework.
1.Verify that the dashboard is completely loaded.
2.Create a report to share with QA team , QA lead, QA Manager with the help of HTML/Allure reporting mechanism.
'''

import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.pageObjects.loginPage import LoginPage

class TestVWOLogin:
    @pytest.fixture()  # Fixture will be the first thing that will run before below testcase execution
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://app.vwo.com")
        driver.maximize_window()
        yield driver
        driver.quit()

    # @allure.feature("VWO Login")
    # @allure.id(1)
    # @allure.story("Positive Testcase in VWO Login")
    # @allure.description("Verify that the valid email, password and we are able to login")
    @pytest.mark.positive  # Benefit of marking is to run it separately
    def test_vwologin(self,driver):  # driver() is passed since it is a fixture as marked above
        loginPage = LoginPage(driver)  # Creating an instance of loginPage & pass driver as a parameter.
        loginPage.login_to_vwo("darshants.1494@gmail.com", "Admin@123")
        time.sleep(4)

        assert "Dashboard" in driver.title
        time.sleep(4)




