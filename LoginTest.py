from selenium import webdriver

#Chrome Config
driverC = webdriver.Chrome(executable_path="D:\\Projects\\Demo_OpencartProject\\BrowserDriver\\chromedriver.exe")

#firefox Config
#driverF = webdriver.Firefox(executable_path="D:\\Projects\\Demo_OpencartProject\\BrowserDriver\\geckodriver.exe")

#Open Link in Browser
driverC.get("https://demo.opencart.com/")
#driverF.get("https://demo.opencart.com/")

