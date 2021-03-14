from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker
import time
faker = Faker()

options = Options()
options.headless = True
options.add_argument('log-level=3')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--no-sandbox')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36')

browser = webdriver.Chrome(options=options, executable_path=r"C:\Users\User\Downloads\chrome\chromedriver.exe")

print("[*] Automation Canva Registration Account + Auto Payment(Paid Script Only)");
print("[*] Author: RJD");
f = open("result.txt", "a+")

#Information

def regis():
    browser.get("https://www.canva.com/signup") 
    
    global i
    name = faker.name_female()
    email = faker.email()
    password = "RJDxSGB123ok"
    reg_click = wait(browser,20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/main/div[6]/div/section/div/div/div/div/div/div/button'))).click()

    print(f"[*] Trying to Registrating Account No {i+1}")
    fill_name = wait(browser,20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/main/div[6]/div/section/div/div/div/div/div/div/div[2]/form/div[1]/input')))
    fill_name.clear()
    fill_name.send_keys(name)

    print(f"[*] Email: {email}|Password: {password}")
    fill_email = wait(browser,20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/main/div[6]/div/section/div/div/div/div/div/div/div[2]/form/div[2]/div/div/div/input')))
    fill_email.clear()
    fill_email.send_keys(email)

    #print("[*] Trying to Fill Password")
    fill_passwd = wait(browser,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/main/div[6]/div/section/div/div/div/div/div/div/div[2]/form/div[3]/input')))
    fill_passwd.clear() 
    fill_passwd.send_keys(password)

    click_submit = wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/main/div[6]/div/section/div/div/div/div/div/div/div[2]/form/button'))) 
    browser.execute_script("arguments[0].click();", click_submit)
    
    print("[*] Registration Success, Saved to result.txt")
    f.write(email + "|"+password)
    browser.get("https://www.canva.com/logout") 
    browser.save_screenshot("screenshot.png")
    time.sleep(5)

def make_count():
    global i
    i = 0
    account = int(input("[*] How many Account: "))
    for i in range(account):
        regis()

make_count()
browser.quit()