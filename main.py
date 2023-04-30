import configparser as cfg
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

random.seed()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

parser = cfg.ConfigParser()
parser.read('config.cfg')
email = parser.get('creds', 'email')
password = parser.get('creds', 'password')

url_login = 'http://langcoglabcgsiitk.in/survey/login.php'
driver = Chrome()
driver.get(url_login)

email_ele = driver.find_element(By.NAME, 'login_username')
password_ele = driver.find_element(By.NAME, 'login_pwd')
email_ele.send_keys(email)
password_ele.send_keys(password)

driver.find_element(By.NAME, 'login').click()

url_home = 'http://langcoglabcgsiitk.in/survey/index.php'
driver.get(url_home)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/div/div/div[1]/div/a'))).click()

xpaths = ['/html/body/main/section/div/form/div/div[3]/label', '/html/body/main/section/div/form/div/input']

for xpath in xpaths:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath))).click()
    print('hi')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div/div/div[3]/button'))).click()

for _ in range(250):
    choice = random.randrange(8)
    driver.find_element(By.ID, f'radio{choice}').click()

    driver.find_element(By.CLASS_NAME, 'btn btn-icon btn-3 btn-success').click()

# driver.close()
print('Done')
