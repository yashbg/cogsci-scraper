import configparser as cfg
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import time

PROJECT_ID = 2
NUM_ITER = 5000
WAIT_TIME = 5
DONT_KNOW_PROB = 0.1
URL_LOGIN = 'http://langcoglabcgsiitk.in/survey/login.php'
URL_PROJECTS = 'http://langcoglabcgsiitk.in/survey/My_project.php'

random.seed()
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_experimental_option("detach", True)

parser = cfg.ConfigParser()
parser.read('config.cfg')
email = parser.get('creds', 'email')
password = parser.get('creds', 'password')

driver = Chrome(options=chrome_options)
driver.get(URL_LOGIN)

email_ele = driver.find_element(By.NAME, 'login_username')
password_ele = driver.find_element(By.NAME, 'login_pwd')
email_ele.send_keys(email)
password_ele.send_keys(password)
driver.find_element(By.NAME, 'login').click()

driver.get(URL_PROJECTS)
driver.find_element(By.XPATH, f'/html/body/main/section[2]/div/div/div[{PROJECT_ID}]/div/a').click() # finish survey

choice_dict = {}
for _ in range(NUM_ITER):
    time.sleep(WAIT_TIME)

    question = driver.find_element(By.XPATH, '/html/body/main/div/section[2]/form/div/div/div/h2/span').get_attribute('innerHTML')
    if question in choice_dict:
        choice = choice_dict[question]
    else:
        if random.random() < DONT_KNOW_PROB:
            choice = 1
        else:
            choice = random.randrange(2, 9)
        choice_dict[question] = choice
    print(question, choice)
    
    driver.find_element(By.XPATH, f'/html/body/main/div/section[2]/form/div/div/div/div[2]/div[3]/label[{choice}]').click() # choice
    driver.find_element(By.XPATH, '/html/body/main/div/section[2]/form/div/div/div/div[2]/div[4]/div/input').click() # next

driver.close()
print('Done')
