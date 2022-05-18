from selenium import webdriver
from selenium.webdriver.common.by import By
# from PIL import image

# Chrome Config
driver = webdriver.Chrome(executable_path="D:\\Projects\\Demo_OpencartProject\\BrowserDriver\\chromedriver.exe")
# firefox Config
# driverF = webdriver.Firefox(executable_path="D:\\Projects\\Demo_OpencartProject\\BrowserDriver\\geckodriver.exe")
# Open Link in Browser
driver.get("https://demo.opencart.com/")
# driverF.get("https://demo.opencart.com/")

# Full Screen
driver.maximize_window()
# Website Link Open
driver.get("https://demo.opencart.com/index.php?route=account/register")
# Find elements on the webpage
driver.find_element(By.ID,'input-firstname').send_keys("Tazin") # First Name
driver.find_element(By.ID,'input-lastname').send_keys("Supti") # Last Name
driver.find_element(By.ID,'input-email').send_keys("t.supti5@gmail.com") # E-mail
driver.find_element(By.ID,'input-telephone').send_keys("01500000000") # Telephone
driver.find_element(By.ID,'input-password').send_keys("1234567890") # Password
driver.find_element(By.ID,'input-confirm').send_keys("1234567890") # Confirm
driver.find_element(By.XPATH,'//*[@id="content"]/form/fieldset[3]/div/div/label[2]').click() # Radio Button
driver.find_element(By.XPATH,'//*[@id="content"]/form/div/div/input[1]').click() # Check Box
# Taking ScreenShot
"""
driver.save_screenshot("img1.png")
Image = Image.open
"""
driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/input[2]').click() # Continue Button
print("Test Done!")


