### How to basically manage proper folder strcucture while designing Web Automation Framework with Page Object Model in Python(Selenium)framework
In Python, creation of folder structure is very simple & straight forward. It's not that difficult as in other programming languages.

1) This is a GIT project. So we are going to add .gitignore file. This file ignores all directories & files which will not be uploaded to GITHUB repository. Pycharm or Intelli-J editors creates some files that we don't want to be pushed to GITHUB repo.
2) Whatever we create all will be as Python Packages.
3) src- This can be renamed as main OR we can keep all packages inside tests also.
    - utils(It help us to read Excel, Database , YAML file & any other files...)
    - pageObjects
      - dashboardPage.py(Page is added in the file name That's why it is called as Page classes)
      - loginPage.py(Page is added in the file name That's why it is called as Page classes)
4) tests- We keep all test related things. Whenever we are writing tests,we should focus on Testcases & Assertions. We keep very limited code such as Abstraction code & Encapsulated code with main focus to write Assertions.
    - vwoLogin
      - vwoLogin.py
5) We will keep Page object classes separately.
6) We need to install dependencies or packages. This is one time activity after creating a new project.
7) We can also move/keep "pageObjects, utils packages" inside tests folder & we can delete src folder.