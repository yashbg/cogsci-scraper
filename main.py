import configparser as cfg
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import time

IMPLICIT_WAIT_TIME = 10
URL_LOGIN = 'http://langcoglabcgsiitk.in/survey/login.php'
URL_PROJECT = 'http://langcoglabcgsiitk.in/survey/survey.php?surveyid=18'
NUM_ITER = 15000
WAIT_TIME = 5
DONT_KNOW_PROB = 0.1
MAX_CHOICE = 7

random.seed()
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True) # keep driver open after script ends

parser = cfg.ConfigParser()
parser.read('config.cfg')
email = parser.get('creds', 'email')
password = parser.get('creds', 'password')

driver = Chrome(options=chrome_options)
driver.implicitly_wait(IMPLICIT_WAIT_TIME)

driver.get(URL_LOGIN)
driver.find_element(By.NAME, 'login_username').send_keys(email) # email
driver.find_element(By.NAME, 'login_pwd').send_keys(password) # password
driver.find_element(By.NAME, 'login').click() # login

driver.get(URL_PROJECT)

choice_dict = {}
for _ in range(NUM_ITER):
    time.sleep(WAIT_TIME)

    question = driver.find_element(By.CLASS_NAME, 'text-success').get_attribute('innerHTML') # question
    if question in choice_dict:
        choice = choice_dict[question]
    else:
        if random.random() < DONT_KNOW_PROB:
            choice = 0
        else:
            choice = random.randrange(1, MAX_CHOICE + 1)
        choice_dict[question] = choice

    driver.find_element(By.CSS_SELECTOR, f'label[for="radio{choice}"]').click() # choice
    driver.find_element(By.CSS_SELECTOR, 'input[class="btn btn-icon btn-3 btn-success"]').click() # next
    print(question, choice)

driver.close()
print('Done')
