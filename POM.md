    Page Object Model

What is a Page Object Model in Selenium?
- It is a design pattern in Selenium that creates an object repository(web elements) for storing all web elements.
It helps reduce code duplication and improves test case maintenance.
https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/

- POM is nothing but a simple class in python selenium.
- In class we have 2 things->Attributes and Methods.
- In POM, every page that we are working on, they will have their own class with `Page Locators in the form of Attributes` & `Page Actions in the form of Methods`


    How many pages are there in web application?
- POM talks about how many pages are present in an application.
- In `app.vwo.com` there are 2 pages(Login page, Dashboard page)

- For example_1:
   In  `app.vwo.com`->We have Login page, Dashboard page.
    If Login= Valid ->Navigate to Dashboard page.
    If Login is not valid ->We will be on same Login page, but with error.
  - In loginpage, there are webelements(in context of POM called as Object repository) such as:
  - email, password, SignUp, Error message(Negative test case), Start Free Trial, Remember me checkbox, Forgot password.

    - For example_2:
        In E-commerce website: `awesomeqa.com/ui` it has Registration, Login, Homepage, Add to Cart, Order ,Payment pages.
    - 6 pages