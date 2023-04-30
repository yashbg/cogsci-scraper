import configparser as cfg
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

random.seed()

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_experimental_option("detach", True)

parser = cfg.ConfigParser()
parser.read('config.cfg')
email = parser.get('creds', 'email')
password = parser.get('creds', 'password')

url_login = 'http://langcoglabcgsiitk.in/survey/login.php'
driver = Chrome(options=chrome_options)
driver.get(url_login)

email_ele = driver.find_element(By.NAME, 'login_username')
password_ele = driver.find_element(By.NAME, 'login_pwd')
email_ele.send_keys(email)
password_ele.send_keys(password)

driver.find_element(By.NAME, 'login').click()

url_projects = 'http://langcoglabcgsiitk.in/survey/My_project.php'
driver.get(url_projects)

finish_survey_ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section[2]/div/div/div[1]/div/a')))
finish_survey_ele.click()

for _ in range(250):
    choice = random.randrange(1, 9)
    choice_ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f'/html/body/main/div/section[2]/form/div/div/div/div[2]/div[3]/label[{choice}]')))
    choice_ele.click()

    next_ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/section[2]/form/div/div/div/div[2]/div[4]/div/input')))
    next_ele.click()

    time.sleep(5)

driver.close()
print('Done')
