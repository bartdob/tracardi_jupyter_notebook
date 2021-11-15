import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

token = '6bb6e68be0e4f983fb522560c340a0b2ce335228e0047734'
notebook_path = 'notebooks/one.ipynb'
base = 'http://127.0.0.1:8888/'
headers = {'Authorization': 'Token 6bb6e68be0e4f983fb522560c340a0b2ce335228e0047734'
           , 'Content-type': 'application/json'}

# http://127.0.0.1:8888/?token=fc6628a48210a7fed3884b1f0fe8aa5b3da1c5f3c3218e15

# api_url = 'http://127.0.0.1:8888/notebooks/one.ipynb'


data = {}


chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--headless")

s=Service(ChromeDriverManager().install())
#
driver = webdriver.Chrome(service=s, chrome_options=chrome_options)
#
# #driver = webdriver.Chrome(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
#                           # options=chrome_options)
#
url = base
#
driver.get(base)
driver.find_element(By.ID, "password_input").send_keys(token)

driver.find_element(By.ID, ("login_submit")).click()
#
response = requests.get(url, headers=headers)
print(url+'/?token='+token)
# # file = json.loads(response.text)


time.sleep(3)

driver.get("http://127.0.0.1:8888/notebooks/one.ipynb")

driver.find_element(By.CSS_SELECTOR, 'body.notebook_app.command_mode:nth-child(2) div.container:nth-child(3) '
                                     'div.navbar:nth-child(2) div.toolbar-inner.navbar-inner.navbar-nobg '
                                     'div.container.toolbar div.btn-group:nth-child(5) '
                                     'button.btn.btn-default:nth-child(1) > span.toolbar-btn-label').click()


time.sleep(50)

# driver.find_element(By.XPATH("//button[contains(.,'Run')]")).click()

# b =driver.find_elements(By.TAG_NAME, "button")
# for i in b:
#     print(i.text)

# print("Button", runAll)
# # r = requests.post(api_url)

# print(response.url)
# print(response.headers)
# print(type(response))
