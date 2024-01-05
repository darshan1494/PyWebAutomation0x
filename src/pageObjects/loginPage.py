# Page classes consists of Page Locators(Attributes) & Page Actions(Methods).

from selenium.webdriver.common.by import By

class LoginPage:
    # Login page should know about Webdriver Init(Initialization). We can initialize something using constructor.
    def __init__(self,driver):
        self.driver = driver

    # Page Locators(Attributes):
    username = (By.ID,"login-username")
    password = (By.NAME,"password")
    submit_button = (By.XPATH,"//button[@id='js-login-btn']")
    error_message  = (By.CSS_SELECTOR, "#js-notification-box-msg")
    # Start Free Trial, Forgot password test cases are skipped as of now

    # Generally in Python the advantage is that, everything can be created as functions.It is like getters.
    # This function returns WebElement->username
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    # Page  Actions(Methods): This is where exact Page  Action starts by using above getters to get Page Locator's values
    def login_to_vwo(self,user, pwd):  # Whoever calls this function should pass username & password from test_vwologin.py
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()
        # get username and sendKeys - email
        # get password and sendKeys - password
        # Click the submit button & Navigate to dashboard page








