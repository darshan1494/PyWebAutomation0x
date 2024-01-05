'''
(Page is added in the file name That's why it is called as Page classes)
Page classes consists of Page Locators(Attributes) & Page Actions(Methods).
Webdriver Init(Initialization)
Custom Functions
There will be no Assertions(They are not Test cases, They are basically known as Page Class.

Every page should know how webdriver is started. Because we need to use By() function.
Until we don't know how driver is started, we cannot call/use driver.find_element(By)
Every Page Class knows about how driver is initializing/started
'''
from selenium.webdriver.common.by import By